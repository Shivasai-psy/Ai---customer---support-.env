# AI Customer Support Assistant

An intelligent customer support assistant built with Python, LangChain, and OpenAI's GPT models. This application classifies customer queries, retrieves relevant information from a knowledge base, and generates personalized responses to provide effective customer support.

## Features

- **Intent Classification**: Automatically detects customer intent (Product Inquiry, Order Status, Returns & Refunds, Technical Support, General Query)
- **Knowledge Base Integration**: Predefined knowledge base with relevant information for each intent category
- **LLM-Powered Responses**: Generates clear, contextual, and empathetic responses using OpenAI's GPT models
- **Conversation Memory**: Maintains conversation context for better understanding and follow-ups
- **Error Handling**: Gracefully handles API errors, invalid inputs, and network issues
- **Clean Architecture**: Modular code structure for easy maintenance and extension
- **Secure API Key Management**: Environment variables for sensitive information
- **Colorful CLI Interface**: Enhanced user experience with color-coded responses

## Technologies Used

- **Python 3.8+**: Core programming language
- **LangChain**: Framework for LLM application development
- **OpenAI GPT-3.5-turbo**: Language model for intent classification and response generation
- **python-dotenv**: Environment variable management
- **colorama**: Terminal color formatting for better UX

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (or equivalent LLM API key)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-customer-support-assistant.git
cd ai-customer-support-assistant
