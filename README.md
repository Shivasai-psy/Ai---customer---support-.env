# 🤖 AI Customer Support Assistant

An AI-powered Customer Support Assistant built using **Python**, **LangChain**, and **Google Gemini/OpenAI API**. The chatbot understands customer queries, identifies the user's intent, retrieves information from a predefined knowledge base, and generates accurate responses while maintaining a natural conversation.

---

## 📌 Features

- AI-powered conversational chatbot
- Intent classification
- Product Inquiry support
- Order Status assistance
- Returns & Refunds support
- Technical Support assistance
  
---

## 🛠 Technologies Used

- Python
- LangChain
- Google Gemini API / OpenAI API
- python-dotenv

---

## 📂 Project Structure

```
AI-Customer-Support-Assistant/
│
├── chat.py
├── intent_classifier.py
├── knowledge_base.py
├── prompts.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/AI-Customer-Support-Assistant.git
cd AI-Customer-Support-Assistant
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project folder.

For Gemini:

```env
GOOGLE_API_KEY=your_api_key_here
```

For OpenAI:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python chat.py
```
---

## 💬 Sample Output

```
<img width="900" height="452" alt="image" src="https://github.com/user-attachments/assets/0ebf61bd-f9e0-4b30-b044-1d6af0e96df3" />
```

---

## 📦 Requirements

```
langchain
langchain-google-genai
google-generativeai
python-dotenv
```

Install using:

```
pip install -r requirements.txt
```

---

## 📄 .gitignore

```
venv/
.env
__pycache__/
*.pyc
.vscode/
.idea/
```

---

## 📄 .env.example

```
GOOGLE_API_KEY=your_api_key_here
```
---

## 🔮 Future Improvements

- Voice support
- Web interface (Flask/Streamlit)
- Database integration
- Multi-language support
- RAG with Vector Database
- Customer authentication

---
