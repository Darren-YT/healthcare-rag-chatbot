# Healthcare RAG Chatbot

Healthcare chatbot powered by Retrieval-Augmented Generation (RAG), Sentence Transformers, Mistral, and Flask.

## Architecture

User Question
→ Embedding Search
→ Healthcare Knowledge Base
→ Mistral LLM
→ Response Generation

## Technologies

- Python
- Flask
- Sentence Transformers
- Ollama
- Mistral
- RAG
- Pandas

## Files

- app.py – Flask application
- chatbot.py – RAG and retrieval logic
- clean_QA.xlsx – Healthcare knowledge base
- templates/index.html – Chat interface
