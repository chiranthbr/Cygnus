from langchain.document_loaders import TextLoader, CSVLoader, Docx2txtLoader, PDFPlumberLoader, PyPDFLoader
from pathlib import Path
import streamlit as st

def getLoaderByExtension(extension: str, pathToDocument):
    if extension in [".txt", ".md"]:
        return TextLoader(pathToDocument)
    elif extension == ".pdf":
        return PyPDFLoader(pathToDocument)
    elif extension == ".csv":
        return CSVLoader(pathToDocument)
    elif extension == ".docx":
        return Docx2txtLoader(pathToDocument)
    
    else:
        return



def fileUploading(uploaded_file):
    extension = uploaded_file.name.split(".")[-1].lower()

    tempFile = "./tempFile." + extension

    with open(tempFile, "wb") as file:
        file.write(uploaded_file.getvalue())


    if uploaded_file.type == "application/pdf":
        return PyPDFLoader(tempFile)
    elif uploaded_file.type == "text/plain":
        return TextLoader(tempFile)
    elif uploaded_file.type == "text/csv":
        return CSVLoader(tempFile)
    elif uploaded_file.type == "text/docx":
        return Docx2txtLoader(tempFile)
    else:
        return




def loadDocument(pathToDocument):
    
    file_path = Path(pathToDocument)
    extension = file_path.suffix.lower()

    loader = getLoaderByExtension(extension, pathToDocument)
    docs = loader.load()

    return docs
