# import streamlit as st
# import json
# import numpy as np
# import faiss
# import spacy
# import google.generativeai as genai
# from PIL import Image
# import streamlit as st

# # ------------------- 1️⃣ Configuration -------------------
# VECTOR_DB_PATH = r"E:\\AI-EDUCATION\\vector_database.index"
# PROCESSED_TEXT_FILE = r"E:\\AI-EDUCATION\\processed_science_data.json"
# EMBEDDINGS_FILE = r"E:\\AI-EDUCATION\\spaCy_embeddings.json"
# LOGO_PATH = r"E:\AI-EDUCATION\AiSPRY logo.jpeg"

# # ------------------- 2️⃣ Load Necessary Files -------------------
# # Page config
# st.set_page_config(page_title="Edubot – Class 10 Science Assistant", layout="wide")

# # Display logo
# try:
#     image = Image.open(LOGO_PATH)
#     st.image(image, use_column_width=True)
# except FileNotFoundError:
#     st.warning("⚠️ Logo not found. Please check the file path.")

# # Title
# st.title("🤖 Edubot – Class 10 Science AI Assistant")

# # image = Image.open(LOGO_PATH)
# st.image(image, width=250)
# st.markdown("## Ask your Class 10 Science Question")
# st.markdown("<style>body {font-family: 'Segoe UI';}</style>", unsafe_allow_html=True)

# # ------------------- 3️⃣ Load Data -------------------
# with open(PROCESSED_TEXT_FILE, "r", encoding="utf-8") as f:
#     processed_text = json.load(f)

# with open(EMBEDDINGS_FILE, "r") as f:
#     embeddings = json.load(f)

# chapter_names = list(embeddings.keys())
# index = faiss.read_index(VECTOR_DB_PATH)

# # ------------------- 4️⃣ Load spaCy Model -------------------
# nlp = spacy.load("en_core_web_lg")

# def get_embedding(text):
#     return nlp(text).vector

# # ------------------- 5️⃣ Gemini Setup -------------------
# genai.configure(api_key="AIzaSyCi4B2bgfvZSbvwEz0jnXgGnEqlzgQ77RE")
# model = genai.GenerativeModel('models/gemini-1.5-flash')

# # ------------------- 6️⃣ FAISS Search -------------------
# def search_faiss(query, top_k=3):
#     query_vector = np.array([get_embedding(query)], dtype='float32')
#     distances, indices = index.search(query_vector, top_k)
#     return [chapter_names[i] for i in indices[0]]

# # ------------------- 7️⃣ Gemini Answer -------------------
# def query_gemini_with_context(query, top_chapters):
#     context = "\n\n".join([f"{ch}:\n{processed_text[ch]}" for ch in top_chapters])
#     prompt = f"""You are a helpful AI tutor for Class 10 Science students.
# Use the following NCERT content to answer the question accurately and simply.

# Context:
# {context}

# Question: {query}

# Answer in simple terms as per NCERT syllabus:"""
#     response = model.generate_content(prompt)
#     return response.text

# # ------------------- 8️⃣ Streamlit Chat UI -------------------
# user_query = st.text_input("❓ Ask a question from NCERT Class 10 Science:")

# if user_query:
#     with st.spinner("Thinking like a genius..."):
#         top_chaps = search_faiss(user_query)
#         answer = query_gemini_with_context(user_query, top_chaps)
#         st.markdown("### 💡 Answer:")
#         st.write(answer)


import streamlit as st
import json
import numpy as np
import faiss
import spacy
import google.generativeai as genai
from PIL import Image

# ------------------- Configuration -------------------
LOGO_PATH = r"E:\AI-EDUCATION\AiSPRY logo.jpeg"
PROCESSED_TEXT_FILE = r"E:\AI-EDUCATION\processed_science_data.json"
EMBEDDINGS_FILE = r"E:\AI-EDUCATION\spaCy_embeddings.json"
VECTOR_DB_PATH = r"E:\AI-EDUCATION\vector_database.index"
GEMINI_API_KEY = "AIzaSyCi4B2bgfvZSbvwEz0jnXgGnEqlzgQ77RE"

# ------------------- Load Logo -------------------
image = Image.open("E:\AI-EDUCATION\AiSPRY logo.jpeg")
st.image(image, width=200)
st.markdown("<h1 style='text-align: center;'>AI-Powered Class 10 Science Chatbot</h1>", unsafe_allow_html=True)

# ------------------- Load NLP Model -------------------
nlp = spacy.load("en_core_web_lg")

# ------------------- Gemini Setup -------------------
genai.configure("AIzaSyCi4B2bgfvZSbvwEz0jnXgGnEqlzgQ77RE")
model = genai.GenerativeModel('models/gemini-1.5-flash')

# ------------------- Load Data -------------------
with open(PROCESSED_TEXT_FILE, "r", encoding="utf-8") as f:
    processed_text = json.load(f)

with open(EMBEDDINGS_FILE, "r", encoding="utf-8") as f:
    embeddings = json.load(f)

chapter_names = list(embeddings.keys())
embedding_matrix = np.array(list(embeddings.values()), dtype='float32')

# ------------------- Load FAISS -------------------
index = faiss.read_index(VECTOR_DB_PATH)

# ------------------- Helper Functions -------------------
def get_embedding(text):
    return nlp(text).vector

def search_faiss(query, top_k=3):
    query_vector = np.array([get_embedding(query)], dtype='float32')
    distances, indices = index.search(query_vector, top_k)
    return [chapter_names[i] for i in indices[0]]

def query_gemini_with_context(query, top_chapters):
    context = "\n\n".join([f"{ch}:\n{processed_text[ch]}" for ch in top_chapters])
    prompt = f"""You are a helpful AI tutor for Class 10 Science students.
Use the following NCERT content to answer the question accurately and simply.

Context:
{context}

Question: {query}

Answer in simple terms as per NCERT syllabus:"""
    response = model.generate_content(prompt)
    return response.text

# ------------------- Streamlit UI -------------------
st.markdown("### Ask your Science Question 👇")

question = st.text_input("Enter your question:")
if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        top_chaps = search_faiss(question)
        answer = query_gemini_with_context(question, top_chaps)
    st.markdown("### 💡 Answer")
    st.write(answer)
