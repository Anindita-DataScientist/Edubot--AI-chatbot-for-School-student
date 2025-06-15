🤖 Edubot – AI-Powered Learning Assistant for NCERT Class 10 Science
An AI chatbot designed to help Class 10 students with syllabus-based questions from the NCERT Science textbook. It combines the power of FAISS, Gemini LLM, and Streamlit for focused and interactive learning support.

## 🎯 Objective
Answer questions only from the NCERT Class 10 Science syllabus.

Help students with simplified, focused, and accurate explanations.

Promote engaged and personalized learning using AI and NLP.

## 🧰 Tech Stack & Tools Used
### 💻 Programming & Platform
Python 3.9

Spyder, Jupyter Notebook

### 📄 Data Handling
PyMuPDF (fitz)

pdfminer.six

### 🧠 NLP & Text Preprocessing
spaCy

NLTK

### 🔎 Embedding & Retrieval
FAISS (Facebook AI Similarity Search)

### 🤖 LLM Integration
Gemini API (Google)

### 🌐 App Development & Deployment
Streamlit

MySQL (optional, for query logging)

## 🔄 Project Workflow (Step-by-Step)
### 1. 📥 Data Collection
Collected Class 10 NCERT Science PDFs (chapter-wise).

Stored in data/class10sciencebook/.

### 2. 📄 Text and Image Extraction
Used PyMuPDF and pdfminer.six to extract:

✅ Text

✅ Diagrams (optional)

Stored results in extracted/.

### 3. 🧹 Text Preprocessing
Performed using spaCy and NLTK:

Tokenization

Lowercasing

Stopword Removal

Special Character and Number Removal

Lemmatization

Stemming

Chunking for context management

All handled in preprocessing/text_cleaning.py

### 4. 📐 Embedding Generation & FAISS Indexing
Generated embeddings using spaCy/Gemini-compatible format.

Created a FAISS vector index for similarity-based text retrieval.

### 5. 🤖 Gemini API Integration
Used Gemini LLM to answer questions.

Prompt includes only retrieved syllabus-based chunks:

"Use this chunk to answer the question only based on it:
[retrieved_text]. Question: [user_query]"

### 6. 💬 Chatbot App with Streamlit
Created interactive UI using Streamlit.

Features:

Question input

Response display

Optional: show retrieved source

File: app/AI_Powered_chatbot.py

### 7. 🧪 Testing & Evaluation
Tested with real NCERT syllabus questions.

Verified for:

Accuracy ✅

Relevance ✅

Readability ✅

Added fallback for off-topic inputs:
"I’m trained only on Class 10 NCERT Science syllabus. Please ask relevant questions."

### 8. 🚀 Deployment Readiness
Fully functional in local environment.

Ready for deployment on Heroku / AWS / GCP.

Easily dockerizable for cloud deployment.

## 🌟 Key Achievements
✅ Accurate, NCERT-aligned responses

✅ Gemini + FAISS = Fast + Relevant

✅ Easy-to-use Streamlit UI

✅ Scalable for other subjects and languages

## 🛠️ How to Run Locally
Follow these steps to set up and run the chatbot:

### 1. Clone the repository
git clone https://github.com/yourusername/edubot-ncert-class10.git
cd edubot-ncert-class10

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the chatbot app
streamlit run app/AI_Powered_chatbot.py
























