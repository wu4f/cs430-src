from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer, Html2TextTransformer
from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import unidecode
import requests
import re
import os

def chunking(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=150)
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
    docs = AsyncHtmlLoader(links).load()
    docs = Html2TextTransformer().transform_documents(docs)
    return clean_documents(docs)

def add_documents(vectorstore, chunks, n):
   for i in range(0, len(chunks), n):
       vectorstore.add_documents(chunks[i:i+n])

if __name__ == '__main__':
    vectorstore = Chroma(
        embedding_function=FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5"),
        persist_directory="./.chromadb"
    )

    cs_website = "https://codelabs.cs.pdx.edu/cs430"
    s = requests.Session()
    headers = {
        'User-Agent' : 'PDXAcademicClient/cs430'
    }
    resp = requests.get(cs_website,headers=headers)
    soup = BeautifulSoup(resp.text,"html.parser")
    links = list({urljoin(cs_website,a['href']) for a in soup.find_all('a', href=True)})

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
