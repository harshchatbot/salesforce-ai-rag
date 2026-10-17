from fastapi import FastAPI , Header , HTTPException , Depends
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import secrets


app = FastAPI()
load_dotenv()  # Load environment variables from .env file

API_KEY=os.getenv("RAG_API_KEY")
'''FastAPI is a class provided by the framework.



app is an instance of that class.
app will register our API routes and handle HTTP requests.'''





class QuestionRequest(BaseModel):
    question: str  
    #this defines expected json response 
    """{
        "question": "What is RAG?"
        }"""
    

@app.get("/health")
def health_check():
    return {"status": "Working Fine"}


def verify_api_key(x_api_key: str | None = Header(default=None)):

    if not API_KEY:
        raise HTTPException(status_code=503 , detail="API authentication not configured")

    if not x_api_key or not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(status_code=401, detail="Unauthorized")
    


@app.post("/ask", dependencies=[Depends(verify_api_key)])
def ask_question(request : QuestionRequest):    
    ditt = {
         "answer" : "You asked: " + request.question
    }

    return ditt



