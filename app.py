from flask import Flask, render_template, request, jsonify
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Access the key like this:
google_api_key = os.getenv("GOOGLE_MAPS_API_KEY")

app = Flask(__name__)

# ✅ Use llama3:instruct model
model = OllamaLLM(model="llama3:instruct")

# ✅ Prompt template (instruct-friendly)
template = """
You are an expert in answering questions about Starbucks.

Here are some relevant customer reviews:
{reviews}

Now answer this question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    if not question.strip():
        return jsonify({"answer": "Please ask a valid question."})

    docs = retriever.invoke(question)
    reviews = "\n".join([doc.page_content for doc in docs])
    response = chain.invoke({"reviews": reviews, "question": question})

    # ✅ Fallback: Add an emoji if none are present in the response
    if not any(char in response for char in ["☕", "😋", "🍩", "🌟", "💬"]):
        response += " ☕"

    return jsonify({"answer": response})


@app.route("/nearby", methods=["POST"])
def nearby_starbucks():
    data = request.get_json()
    lat = data.get("lat")
    lng = data.get("lng")

    # 🟤 Use keyword=starbucks and rankby=distance for most relevant Starbucks stores
    params = {
        "location": f"{lat},{lng}",
        "keyword": "starbucks",
        "rankby": "distance",
        "type": "cafe",
        "key": google_api_key,
    }

    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params
    )

    places = response.json().get("results", [])[:5]

    result = []
    for place in places:
        result.append(
            {
                "name": place["name"],
                "address": place.get("vicinity", "No address"),
                "rating": place.get("rating", "N/A"),
                "lat": place["geometry"]["location"]["lat"],
                "lng": place["geometry"]["location"]["lng"],
            }
        )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
