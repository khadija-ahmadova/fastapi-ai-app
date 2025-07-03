import os
from .ai.gemini import Gemini
from pydantic import BaseModel
from fastapi import Depends, FastAPI
from auth.dependencies import get_user_identifier
from auth.throttling import apply_rate_limit

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

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY env variable not set.")

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)


# --- pydantic models ---
class ChatRequest(BaseModel):
    prompt: str # {"prompt" : "..."}

class ChatResponse(BaseModel):
    response: str # return {"response": "..."}


# --- api endpoints ---
@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, user_id: str = Depends(get_user_identifier)):
    apply_rate_limit(user_id)
    response_text = ai_platform.chat(request.prompt)
    return ChatResponse(response=response_text)