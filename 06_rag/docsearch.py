from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import readline

from langchain_community.embeddings import FastEmbedEmbeddings

vectorstore = Chroma(
    embedding_function=FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5"),
    persist_directory="./.chromadb"
)

def search_db(query):
    docs = vectorstore.similarity_search(query)
    print(f"Query database for: {query}")
    if docs:
        print(f"Closest document match in database: {docs[0].metadata['source']}")
        print(f"Document content is: {docs[0].page_content}")
    else:
        print("No matching documents")

print("RAG database initialized.")
retriever = vectorstore.as_retriever()
document_data_sources = set()
for doc_metadata in retriever.vectorstore.get()['metadatas']:
    document_data_sources.add(doc_metadata['source']) 
for doc in document_data_sources:
    print(f"  {doc}")

print("This program queries documents in the RAG database that are similar to whatever is entered.  A blank query exits the program.")
while True:
    line = input(">> ")
    if line:
        search_db(line)
    else:
        break
