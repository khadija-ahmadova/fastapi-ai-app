# FastAPI AI App

- user can send a text and the backend will use AI model to answer
- built with Python and FastAPI
- Gemini is used for AI Model
- rate limiter prevents users from sending too many requests
- user authentication with JWT tokens


## Setting up

Create and activate virtual environment
```
python -m venv venv
source venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Set up Gemini API key as environment variable
```
export GEMINI_API_KEY="your_gemini_api_key"
```

## Usage
To run the application
```
uvicorn src.main:app --reload
```

To interact with the API using auto-generated FastAPI documentation, go to http://127.0.0.1:8000/docs

## Configuration

You can configure system prompt by editing `src/prompts/system_prompt.md` file

To modify rate limits, change constants in `src/auth/throttling.py`

To use a different AI model, create a new class that inherits from `AIPlatform` and implement the `chat` method

## Architecture

- `src/main.py`: the main FastAPI application file
- `src/ai/base.py`: defines `AIPlatform` interface
- `src/ai/gemini.py`: implementation of the `AIPlatform` interface for Gemini
- `src/prompts/system_prompt.md`: system prompt for AI
- `src/auth/dependencies.py`: jwt decoding and user identification
- `src/auth/throttling.py`: provides a simple in-memory rate limiter with different limits for authenticated and unauthenticated users