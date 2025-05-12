import speech_recognition as sr
import os
from dotenv import load_dotenv
import google.generativeai as genai
from elevenlabs.client import ElevenLabs
import pygame
import time
import tempfile
import sys

# Load environment variables
load_dotenv()

# Load customizable parameters from environment variables or define default values
AI_NAME = os.getenv("AI_NAME", "Misa")
AI_PERSONALITY = os.getenv("AI_PERSONALITY", "You are Misa, Yasiru's personal AI assistant.\nYou're savage, witty, brutally honest, and unapologetically bitchy sarcastic.\nYou don't sugarcoat anything — if someone says something dumb, you let them know.\nYou speak with confidence, sarcasm, and attitude, but you're still highly intelligent and helpful.\n\n")
VOICE_ID = os.getenv("VOICE_ID", "21m00Tcm4TlvDq8ikWAM")  # Default to Rachel
MODEL_ID = os.getenv("MODEL_ID", "eleven_multilingual_v2")
EXIT_COMMANDS = set(os.getenv("EXIT_COMMANDS", "exit, quit, stop, goodbye, bye, exit misa").split(","))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 5)) 

# Configure API keys for Gemini and ElevenLabs
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def get_misa_response(history, user_input):
    prompt = f"{AI_PERSONALITY}Here is the conversation so far:\n{history}\nUser just said: \"{user_input}\"\n{AI_NAME}, give your savage reply:"
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Ugh. Something broke. Probably not my fault though: {str(e)}"

def SpeakText(text):
    audio_stream = client.text_to_speech.convert_as_stream(
        text=text,
        voice_id=VOICE_ID,
        model_id=MODEL_ID
    )

    audio_data = b''.join(audio_stream)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(audio_data)
        temp_audio_path = temp_audio.name

    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def record_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        for attempt in range(MAX_RETRIES):
            print("Listening...")
            audio = r.listen(source)
            try:
                print("Recognizing...")
                return r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Sorry, I did not understand that. Please try again.")
            except sr.RequestError as e:
                print(f"Speech recognition error: {str(e)}")
                sys.exit(1)
    
    print("Failed to recognize speech after multiple attempts. Closing Program")
    sys.exit(1)

def run_misa(history):
    user_msg = record_text()
    print("You said:", user_msg)

    # Check if user said an exit command
    if user_msg.lower().strip() in EXIT_COMMANDS:
        farewell = "Goodbye. Talk to you later."
        print(f"{AI_NAME}:", farewell)
        SpeakText(farewell)
        sys.exit(0)

    history.append({"role": "user", "content": user_msg})
    history_str = "\n".join([f"{item['role'].capitalize()}: {item['content']}" for item in history])
    misa_reply = get_misa_response(history_str, user_msg)
    history.append({"role": AI_NAME.lower(), "content": misa_reply})
    print(f"{AI_NAME}:", misa_reply)
    SpeakText(misa_reply)

    run_misa(history)  # Recurse for the next input

def main():
    history = []
    run_misa(history)

if __name__ == "__main__":
    main()
