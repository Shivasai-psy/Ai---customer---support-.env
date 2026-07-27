# Ai-customer-support
# 🤖 AI Customer Support Assistant

A modular, conversational AI assistant built with **Python** and **LangChain** that understands customer queries, classifies intent, retrieves relevant knowledge, and generates helpful responses using an LLM.

---

## ✨ Features

- **Intent Classification** — Automatically categorizes queries into:
  - Product Inquiry
  - Order Status
  - Returns & Refunds
  - Technical Support
  - General Query
- **Knowledge Retrieval** — Fetches relevant context from a predefined knowledge base
- **Conversational Memory** — Maintains context across multi-turn conversations
- **Graceful Error Handling** — Handles API failures, network issues, and empty input
- **Modular Architecture** — Clean separation of concerns across files
- **Secure API Key Management** — Uses `.env` file (never hardcoded)

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.9+ | Core language |
| LangChain | LLM orchestration & prompt management |
| OpenAI API | LLM provider (GPT-4o-mini) |
| python-dotenv | Environment variable management |

---

## 📦 Installation

### 1. Clone or create the project directory

```bash
mkdir ai-customer-support
cd ai-customer-support
