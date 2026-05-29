# chatbot.py
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import ollama

# Load dataset
df = pd.read_excel("clean_QA.xlsx")

# Embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
question_embeddings = embed_model.encode(df["question"].tolist(), convert_to_tensor=True)

# RAG + Mistral generation
def summarize(text, max_chars=300):
    """Reduce text length so Mistral won't overflow."""
    prompt = f"Summarize this medical content in under {max_chars} characters:\n{text}"
    response = ollama.generate(model="mistral", prompt=prompt)
    return response["response"].strip()

def generate_answer(question, summary_text):
    prompt = f"""
Using the following medical information, answer the user's question clearly, friendly, and accurately.

Information: {summary_text}

User question: {question}

Answer:
"""
    response = ollama.generate(model="mistral", prompt=prompt)
    return response["response"].strip()

def chatbot(question):
    # Step 1: find nearest Q
    q_emb = embed_model.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(q_emb, question_embeddings)[0]
    idx = scores.argmax().item()
    score = scores[idx].item()

    # Step 2: threshold
    if score >= 0.45:
        source = df.iloc[idx]["answer"]
        summary = summarize(source)
        return generate_answer(question, summary)
    else:
        prompt = f"Answer this general health question clearly:\n{question}"
        response = ollama.generate(model="mistral", prompt=prompt)
        return response["response"].strip()
