from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ARLinus API", version="1.0")

class Question(BaseModel):
    text: str
    level: str  # primaire | college | lycee | universite

@app.get("/")
def home():
    return {
        "name": "ARLinus",
        "status": "online",
        "message": "API éducative active"
    }

@app.post("/ask")
def ask_ai(question: Question):
    # ⚠️ temporaire : réponse simple (on branchera Phi-3 après)
    return {
        "question": question.text,
        "level": question.level,
        "answer": "Je vais t'aider étape par étape. (IA en cours d'intégration)"
    }
