from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from db.session import get_db
from llm.agent import process_question

app = FastAPI(title="E-Commerce AI Agent")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest, db=Depends(get_db)):
    try:
        return process_question(request.question, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/")
def read_root():
    return {"message": "E-Commerce AI Agent is running! Visit /docs for API UI"}
