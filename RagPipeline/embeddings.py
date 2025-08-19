from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def embedAndVectoriseDocument(document):
    # model_name = "sentence-transformers/all-MiniLM-L6-v2" 

    embeddings = HuggingFaceEmbeddings(
        model_name="local_models/all-MiniLM-L6-v2"
    )

    vector = FAISS.from_documents(document, embeddings)#, normalize_L2=True)        # Store in a vector FAISS
    return vector