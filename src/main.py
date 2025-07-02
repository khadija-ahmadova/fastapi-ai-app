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


# --- api endpoints ---
@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("chat/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # TODO: implement ai intergration
    response_text = "..."
    return ChatResponse(response=response_text)