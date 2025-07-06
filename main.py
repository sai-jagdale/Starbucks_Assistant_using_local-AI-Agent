from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3:instruct", temperature=0.7, max_tokens=150)
# ✅ Prompt template (instruct-friendly)
template = """
You are a friendly, engaging Starbucks Assistant.

✅ Always include relevant emojis such as ☕, 😋, 🌟, 💬, or 🍩 to make the answer fun.
✅ Keep the tone casual and inviting.
✅ Limit the answer to 42-3 short sentences.
Please include relevant emojis (like ☕, 🍩, 😋, 💬, 🌟) to make your answers fun and expressive.

Do not forget the emojis – they are part of your personality! 😉✨

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

Avoid unnecessary details.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\\---------------------------------------------")
    question = input("Ask your question about Starbuks (q to quit)")
    print("\\------------------------------------------")
    if question == "q":
        break

    docs = retriever.invoke(question)
    reviews = "\n".join([doc.page_content for doc in docs])
    result = chain.invoke({"reviews": reviews, "question": question})
    print("Answer:\n", result, "\n")
