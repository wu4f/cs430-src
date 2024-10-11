from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import readline

vectorstore = Chroma(
     persist_directory="./.chromadb",
     embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001", task_type="retrieval_query")
)

retriever = vectorstore.as_retriever()

prompt_template = """You are an assistant for question-answering tasks. Use the following context to answer the question.  Provide the source URLs of the context you used to perform the task and instruct the user to visit them for more information.  If you don't know the answer, just say that you don't know. 

Question: {question} 

Context: {context} 

Answer: """

# create a prompt example from above template
prompt = PromptTemplate(
    input_variables=["question"],
    template=prompt_template
)

llm = GoogleGenerativeAI(model="gemini-1.5-flash",temperature=0)

def format_docs(docs):
    output = "\n\n".join(doc.page_content for doc in docs)
    sources = {doc.metadata['source'] for doc in docs}
    source_list = "\nSource: ".join(source for source in sources)
    return output+source_list

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("Welcome to my RAG application.  Ask me a question and I will answer it from the documents in my database shown below.  A blank query exits the program.")
# Iterate over documents and dump metadata
document_data_sources = set()
for doc_metadata in retriever.vectorstore.get()['metadatas']:
    document_data_sources.add(doc_metadata['source']) 
for doc in document_data_sources:
    print(f"  {doc}")

while True:
    line = input("llm>> ")
    if line:
        result = rag_chain.invoke(line)
        print(result)
    else:
        break
