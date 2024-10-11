from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import unidecode
import requests
import re
import os

def chunking(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_documents(documents)
    return chunks

def clean_text(text):
    text = unidecode.unidecode(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def clean_documents(documents):
    for doc in documents:
        doc.page_content = clean_text(doc.page_content)
    return documents

def scrape_articles(links):
    """Scrapes list of links, extracts article text, returns Documents"""
    # Request header template

    # Scrape list of links
    loader = AsyncHtmlLoader(links)
    docs = loader.load()
    # Extract article tag
    transformer = BeautifulSoupTransformer()
    docs_tr = transformer.transform_documents(
        documents=docs, tags_to_extract=["article"]
    )
    clean_documents(docs_tr)
    return docs_tr

def add_documents(vectorstore, chunks, n):
   for i in range(0, len(chunks), n):
       vectorstore.add_documents(chunks[i:i+n])

if __name__ == '__main__':
    vectorstore = Chroma(
            embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001", task_type="retrieval_query"),
            persist_directory="./.chromadb"
    )

    cs_website = "https://www.pdx.edu/computer-science"
    resp = requests.get(cs_website)
    soup = BeautifulSoup(resp.text,"html.parser")
    links = list({urljoin(cs_website,a['href']) for a in soup.find_all('a', href=True) if any(['computer-science' in a['href'], 'security' in a['href']])})

    documents = scrape_articles(links)

    chunks = chunking(documents)
    add_documents(vectorstore, chunks, 300)

    print("RAG database initialized with the following sources.")
    retriever = vectorstore.as_retriever()
    document_data_sources = set()
    for doc_metadata in retriever.vectorstore.get()['metadatas']:
        document_data_sources.add(doc_metadata['source']) 
    for doc in document_data_sources:
        print(f"  {doc}")
