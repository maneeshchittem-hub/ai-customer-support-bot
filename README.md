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

```text
User
 ↓
Streamlit Chatbot
 ↓
LangChain Agent
 ↓
Tool / Function Calling
 ↓
SQLite Database
 ↓
Order Information
 ↓
Gemini
 ↓
Final Answer ```
