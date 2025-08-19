import requests
import streamlit as st
from langchain.document_loaders import TextLoader, CSVLoader, Docx2txtLoader, PyPDFLoader


from RagPipeline.main import BuildQAChain

# if "uploaded_file" not in st.session_state:
#     st.session_state.uploaded_file = st.file_uploader(type=["txt", 'pdf', "docx", "csv", ], accept_multiple_files=False, label="Upload File", key=123)

# # st.session_state.uploaded_file = st.file_uploader(type=["txt", 'pdf', "docx", "csv", ], accept_multiple_files=False, label="Upload File", key=123)
# uploaded_file = st.session_state.uploaded_file

uploaded_file = st.file_uploader(type=["txt", 'pdf', "docx", "csv", ], accept_multiple_files=False, label="Upload File")

def checkOllamaInstalled():
    try:
        request = requests.get("http://localhost:11434/api/tags", timeout=2)
        if request.status_code == 200:
            return True
    except Exception:
        return False
    
if not checkOllamaInstalled():
    st.error("Ollama is not running (or) it is not installed. Make sure it is installed and run `ollama serve` before using the app!!")
    st.stop()

# @st.cache_resource
def loadQAChain():
    checkOllamaInstalled()
    if uploaded_file is not None:
        return BuildQAChain(uploaded_file)

# QA chain
qa_chain = loadQAChain()

query = st.text_input("Ask something:")

if query:
    answer = qa_chain.invoke({"input": query})
    st.write(answer)

# import gradio as gd

# qa_chain = BuildQAChain()

# def responseToQuery(query, chat_history=None):
#     if not query:
#         return "Please ask question"
#     result = qa_chain.invoke({"input": query})
#     return result

# gd.ChatInterface(
#     fn=responseToQuery,
#     chatbot=gd.Chatbot(height=500, type="messages"),
#     textbox=gd.Textbox(placeholder="Ask me anything", scale=7,container=False),
#     title="Answering machine",
#     examples=["Who is Percy Jackson?", " What is the title of the short story that features both Carter Kane and Percy Jackson?", "What is Percy Jackson's diagnosis mentioned in the text?", "What is the name of Grover's summer address?", "What is the name of the place where Percy, Annabeth, and Grover encounter Medusa?"],
#     cache_examples=True,

# ).launch(share=False)