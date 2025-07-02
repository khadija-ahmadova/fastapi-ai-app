import os
from fastapi import FastAPI
from pydantic import BaseModel

# --- app initialization
app = FastAPI()

# --- ai configuration ---
def load_system_prompt():
    try:
        with open("src/prompts/system_prompt.md", "r") as f:
            return f.read()
    except FileNotFoundError:
            return None
    
system_prompt = load_system_prompt()

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