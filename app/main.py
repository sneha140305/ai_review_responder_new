from fastapi import FastAPI
from app.ai_responder import generate_reply

app = FastAPI(title="AI Review Responder")

@app.get("/")
def root():
    return {"message": "AI Review Responder is running!"}

@app.post("/generate-reply/")
def create_reply(review: str):
    reply = generate_reply(review)
    return {"review": review, "reply": reply}
