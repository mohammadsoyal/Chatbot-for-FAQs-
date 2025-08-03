# Chatbot-for-FAQs-
This is a simple and intelligent chatbot built with **Python**, **NLTK**, and **Streamlit** that answers frequently asked questions (FAQs) about a product or service using **semantic similarity**.

---

## 📦 Features

✅ Load FAQs from a CSV file  
✅ NLP-based preprocessing (tokenization, stopword removal)  
✅ TF-IDF + Cosine Similarity for matching  
✅ Confidence score display  
✅ Simple and clean Streamlit UI  
✅ Upload your own FAQ CSV  
✅ Clear chat history anytime

---

## 🖼️ Preview

![FAQ Chatbot Screenshot](https://via.placeholder.com/800x400?text=Streamlit+FAQ+Chatbot+Demo)

---

## 📁 Project Structure

```
FAQChatbot/
├── Faqs_100.csv            # Sample CSV file with FAQs
├── chatbot.py              # Main Streamlit chatbot app
├── README.md               # Project documentation
```

---

## 🛠️ Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- pandas
- nltk
- scikit-learn

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/FAQChatbot.git
cd FAQChatbot
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, manually install:

```bash
pip install streamlit pandas nltk scikit-learn
```

4. **Download NLTK resources:**

The script will automatically download `punkt` and `stopwords`, or you can do it manually:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🚀 Running the App

```bash
streamlit run chatbot.py
```

Then open the link it gives (usually `http://localhost:8501`) in your browser.

---

## 📝 CSV Format

Make sure your FAQ CSV has the following columns:

| question                      | answer                              |
|------------------------------|-------------------------------------|
| What is the battery life?    | The battery lasts up to 10 hours.   |
| Does it support fast charge? | Yes, it supports 30W fast charging. |

---

## 📌 Notes

- If no CSV is uploaded via the UI, it uses the default path:  
  `D:\AI INTERNSHIP\chatbotfaq\FAQChatbot\Faqs_100.csv`
- Confidence score is displayed for each response.
- You can clear the chat anytime.

---

## 🧠 Future Improvements

- Add voice input/output  
- Support for multilingual questions  
- Deploy on Streamlit Cloud or Render  
- Integrate with a real product API

---

## 🧑‍💻 Author

Mohammad Soyal  
[LinkedIn](https://linkedin.com) • [GitHub](https://github.com/yourusername)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
