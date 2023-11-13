# uvicorn main:app
# uvicorn main:app --reload
# venv\Scripts\activate

# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config 
import openai

# Custom function imports
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.text_to_speech import convert_text_to_speech
from fastapi import Depends, FastAPI, HTTPException

SECRET_KEY = "439c1b9ad8b3636d32bcf785ecce2bf7361cc523dacb7ecafa0f3888937029ab"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Get Environment Vars
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Initiate app
app = FastAPI()

db = {
    "majid": {
        "username": "majid",
        "full_name": "Majid Alamoudi",
        "email": "majidamoudy15@gmail.com",
        "hashed_password": "",
        "disabled": False
    }
}

# CORS - Origins
origins = [
    "https://localhost:5173",
    "http://localhost:5173",
    "https://localhost:5174",
    "http://localhost:5174",
    "https://localhost:4173",
    "https://localhost:4173",
    "https://localhost:4174",
    "http://localhost:4174",
    "https://localhost:3000",
    "http://localhost:3000",
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"] 
)

# Check health
@app.get("/")
async def check_health():
    return {"message": "Healthy"}

# Reset messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation reset"}

# Get audio
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # Get saved audio 
    # audio_input = open("voice.mp3", "rb")

    # Save file from Frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Get ChatGPT response
    chat_response = get_chat_response(message_decoded)

    # Store messages
    store_messages(message_decoded, chat_response)

    # Guard: Ensure message decoded
    if not chat_response:
        raise HTTPException(status_code=400, detail="Failed to get chat response")

    # Convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)

    # Guard: Ensure output
    if not audio_output:
        raise HTTPException(status_code=400, detail="Failed to get Eleven Labs audio response")
    
    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")

    return "Done"




