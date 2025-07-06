# ☕ Starbucks Assistant — AI Chatbot Powered by LLaMA 3 & LangChain

Ask anything about Starbucks — Get intelligent, summarized, and relevant answers using LLaMA 3 (via Ollama), LangChain, and Retrieval-Augmented Generation (RAG) 🔍☕
Works fully offline. Runs in your browser with a friendly coffee-themed UI.

## 🌟 Features

- 🤖 **Ask Anything About Starbucks** – From drinks and rewards to sustainability, store policies, and fun facts.
- 🧠 **Powered by LLaMA3 (via Ollama)** – Runs locally using Meta's LLaMA3-8B model with fast response and full control.
- 🔍 **RAG-based Chatbot** – Uses Retrieval Augmented Generation for accurate, context-rich responses.
- 💬 **Engaging Coffee-Themed UI** – Chat UI styled with Starbucks color palette, emojis, and rounded messages.
- ☕ **“Brewing” Typing Animation** – Visual feedback while generating the answer.
- 📝 **4-5 Sentence Answers** – Optimized for clarity and brevity.
- ✅ **Local & Private** – Works entirely on your machine; no cloud APIs needed.

## 📦 Technologies Used

| Tool / Library         | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| 🦙 **llama3:instruct** | LLM from Meta, fine-tuned for instruction-based Q&A                     |
| 🧠 **Ollama**          | Framework to run LLMs locally with 1-line setup                         |
| 🔗 **LangChain**       | Chaining inputs, context and model logic                                |
| 📚 **LangChain-Chroma**| Vector store to store & retrieve relevant reviews (retriever)           |
| 🌐 **Flask**           | Lightweight Python web framework for hosting the chat UI                |
| 📊 **Pandas**          | Load and manipulate the CSV review dataset                              |
| 🧠 **RAG**             | Retrieval Augmented Generation – smartly fetches relevant context       |
| 🎨 **Tailwind CSS**    | Utility-first styling to match the coffee/Starbucks aesthetic           |
| 📁 **Custom Dataset**  | Starbucks customer reviews (CSV file) used as knowledge base            |

## 🧠 How It Works

1. You type a question.
2. The backend **retrieves relevant Starbucks reviews** using vector similarity from a Chroma vector store.
3. The **question + top reviews** are passed to the **llama3:instruct** model through **LangChain**.
4. The **response** is limited to 4-5 concise, informative sentences with some ☕ emojis for engagement.
5. The UI displays the result with a coffee-themed animation and style.

## 📁 Project Structure

Starbucks_Assistant/
│
├── starbucks_reviews_data.csv # Dataset of Starbucks reviews (used in RAG)
│
├── app.py # Flask app serving the chatbot interface
├── main.py # CLI-based question tester for debugging
├── vector.py # Vector retriever using LangChain + Chroma
│
├── _pycache_
│
├── chroma_langchain_db
│  └── chroma.sqlite3
│ 
├── venv/
│
├── static/
│ ├── Starbucks-logo.png # Circular Starbucks logo
│
├── templates/
│ └── index.html # Chat UI page
│
├── Screenshots(Using UI)/
├── Screenshots(without UI only , on local system)/
│ 
├── requirements.txt # Python dependencies
└── README.md # This file

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/starbucks-assistant.git
cd starbucks-assistant
```
### 2. Install dependencies in a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Download the model (LLaMA 3)
Ensure [Ollama](https://ollama.com/) is installed and running, then:
```bash
ollama run llama3:instruct
```
### 4. Add your data file
Place your CSV file (`starbucks_reviews_data.csv`) in the `vector.py` path.
---
### 5. Run the Flask App
```bash
python main.py
```
Visit: `http://localhost:5000` in your browser.

## 💡 Sample Questions to Try
🥤 What are the most loved Starbucks drinks?
🍪 Do Starbucks stores sell food items too?
💰 What is the price range of Starbucks coffee?
🏪 How is the ambience at Starbucks locations?
🌍 Where does Starbucks source its coffee beans?

## License

This repository is licensed under the **All Rights Reserved** terms.  
You are free to **view** the code, but **reproduction, modification, or reuse** is **not permitted** without permission.  





