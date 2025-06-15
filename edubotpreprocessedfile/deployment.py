import streamlit as st
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import GooglePalm

# Set page config
st.set_page_config(page_title="NCERT Class 10 Science Chatbot", layout="centered")

# Load logo
logo_path = "E:/AI-EDUCATION/WhatsApp Image 2025-04-10 at 1.17.14 PM.jpeg"
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src="file://{logo_path}" width='300'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🔬📘 NCERT Class 10 Science Chatbot")
st.markdown("Ask any question from your syllabus!")

# Initialize the chatbot only once
@st.cache_resource
def initialize_bot():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="your_google_api_key_here")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    llm = GooglePalm(google_api_key="your_google_api_key_here", temperature=0.5)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=new_db.as_retriever())
    return qa_chain

qa_bot = initialize_bot()

# Chat input
query = st.text_input("Ask a question from Class 10 Science 📖", placeholder="e.g., What is Ohm's law?")

# Response
if query:
    with st.spinner("Thinking..."):
        response = qa_bot.run(query)
        st.success(response)

