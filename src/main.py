import os
from fastapi import FastAPI
from pydantic import BaseModel

# initialize app
app = FastAPI()

# --- pydantic models ---
class ChatRequest(BaseModel):
    prompt: str # {"prompt" : "..."}

class ChatResponse(BaseModel):
    response: str # return {"response": "..."}