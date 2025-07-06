from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv(
    r"C:\Users\Rajendra\Desktop\Projects\AI_Agent_Local\starbucks_reviews_data.csv"
)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []

    for i, row in df.iterrows():
        document = Document(
            page_content=str(row["Review"]) + " Rating : " + str(row["Rating"]),
            metadata={"rating": row["Rating"], "date": row["Date"]},
        )
        documents.append(document)

vector_store = Chroma(
    collection_name="Starbuks_Reviews",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents)

retriever = vector_store.as_retriever(search_kwargs={"k": 4})
