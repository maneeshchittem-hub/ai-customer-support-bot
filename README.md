# 🤖 AI Customer Support Bot with Live Order Tracking

An AI-powered customer support chatbot that helps users with order tracking, delivery status, returns, refunds, cancellations, and company policies.

The application uses **RAG (Retrieval-Augmented Generation)** to answer company-policy questions and **LangChain tool/function calling** to retrieve live order information from a SQLite database.

## 🎯 Difficulty

**Medium**

## 🚀 Live Demo

https://orderpilot-ai.streamlit.app

## ✨ Features

- 🤖 AI-powered customer support chatbot
- 📦 Real-time order tracking using SQLite
- 🚚 Delivery status checking
- 🔄 Return policy lookup
- 💰 Refund policy lookup
- ❌ Order cancellation policy
- 📋 Company policy questions
- 🔎 RAG-based document retrieval
- 🛠️ LangChain function/tool calling
- 🕘 Recent questions
- 🧹 Clear chat functionality
- 💬 ChatGPT-style conversation interface
- 🎨 Custom Streamlit UI with CSS

## 🧠 How It Works

The application handles different types of customer questions using different approaches.

### Order-related questions
User
1. Customer asks: "Where is my order ORD1001?"
2. Streamlit Chatbot
   → Receives the customer's question
3. LangChain Agent
   → Understands the question
   → Identifies it as an order-related question
4. Tool / Function Calling
   → Calls the get_order() function
5. SQLite Database
   → Searches for order ID ORD1001
6. Order Information
   → Returns order ID, product, status, and delivery date
7. Gemini
   → Converts the database information into a simple answer
8. Final Answer
   → Chatbot displays the answer to the customer
## Tech Stack

- Python
- Streamlit
- Gemini
- LangChain
- RAG
- FAISS
- SQLite

  ## ```bash
>pip install -r requirements.txt

>streamlit run app.py
