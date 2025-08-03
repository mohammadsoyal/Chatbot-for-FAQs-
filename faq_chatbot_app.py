import streamlit as st
import pandas as pd
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Page config
st.set_page_config(page_title="🤖 FAQ Chatbot", page_icon="💬")
st.title("🤖 Product FAQ Chatbot")
st.markdown("Ask me anything related to the product! 📱💡")

# Chat history state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []

# File upload
st.sidebar.header("📂 Upload FAQ CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Load FAQs
@st.cache_data
def load_faqs(file):
    return pd.read_csv(file)

# Preprocessing
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return " ".join([word for word in tokens if word not in stop_words and word not in string.punctuation])

def setup_faq(file):
    df = load_faqs(file)
    df["processed_question"] = df["question"].apply(preprocess)
    vector = TfidfVectorizer()
    matrix = vector.fit_transform(df["processed_question"])
    return df, vector, matrix

# Setup model
faq_df = None
vectorizer = None
X = None

if uploaded_file:
    try:
        faq_df, vectorizer, X = setup_faq(uploaded_file)
    except:
        st.error("❌ Error loading the file. Make sure it has 'question' and 'answer' columns.")
else:
    default_path = "D:\\AI INTERNSHIP\\chatbotfaq\\FAQChatbot\\Faqs_100.csv"
    faq_df, vectorizer, X = setup_faq(default_path)

# Get best matching answer
def get_best_match(user_input):
    cleaned = preprocess(user_input)
    vec = vectorizer.transform([cleaned])
    similarities = cosine_similarity(vec, X)
    idx = similarities.argmax()
    score = similarities[0][idx]
    if score < 0.2:
        return "🤖: Sorry, I couldn't understand your question.", score
    return f"🤖: {faq_df.iloc[idx]['answer']}", score

# User Input
user_input = st.text_input("💬 Ask a question:", placeholder="e.g., What is the warranty period?")

# Handle response
if user_input:
    answer, confidence = get_best_match(user_input)
    st.session_state.chat_history.append((user_input, answer, confidence))

# Display Chat History
st.subheader("📝 Chat History")
for user_q, bot_a, conf in reversed(st.session_state.chat_history):
    st.markdown(f"**🧑 You:** {user_q}")
    st.markdown(f"{bot_a}")
    st.markdown(f"🧠 Confidence: `{round(conf * 100, 2)}%`")
    st.markdown("---")