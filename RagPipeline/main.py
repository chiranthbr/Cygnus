from .dataLoading import fileUploading
from .embeddings import embedAndVectoriseDocument
from .retriever import retreiveFromVector

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate

uploaded_file = None

def getUploadedFile(uploaded):
    global uploaded_file
    uploaded_file = uploaded

def BuildQAChain():
    print(uploaded_file.name)

    docs = fileUploading(uploaded_file)

    document = docs.load()


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )

    split_docs = text_splitter.split_documents(documents=document)

    vector = embedAndVectoriseDocument(split_docs)

    retriever = retreiveFromVector(vector)

    llm = OllamaLLM(model="mistral")

    prompt = ChatPromptTemplate.from_template(
        "Answer the question using the context:\n\n{context}\n\nQuestion: {input}"
    )

    document_chain = create_stuff_documents_chain(llm, prompt)

    qa_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=document_chain)

    return qa_chain
