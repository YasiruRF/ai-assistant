
# 🎤 Customizable Voice AI Assistant (Misa AI)

This Python project is a fully voice-controlled AI assistant, powered by:

* **Google Gemini 1.5 Flash** for savage and sarcastic natural language generation
* **ElevenLabs** for high-quality, customizable text-to-speech
* **SpeechRecognition** for capturing your voice input
* **Pygame** for audio playback

---

## ✅ Features

* 🎙️ Voice-based input using microphone
* 🧠 AI-generated responses with customizable tone/personality
* 🔊 Realistic speech synthesis with ElevenLabs
* 🔁 Continuous conversation loop
* 🔧 Highly customizable via `.env` file

---

## 🛠️ Setup Instructions

### 1. **Install Dependencies**

```bash
pip install -r requirements.txt
```

Required packages:

```txt
SpeechRecognition
pygame
python-dotenv
google-generativeai
elevenlabs
```

### 2. **Configure Environment Variables**

Create a `.env` file in your project directory with the following:

```env
GEMINI_API_KEY=your_google_gemini_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

AI_NAME=Misa
AI_PERSONALITY=You are Misa, Yasiru's personal AI assistant. You're witty, sarcastic, brutally honest, and confident.
VOICE_ID=21m00Tcm4TlvDq8ikWAM
MODEL_ID=eleven_multilingual_v2
EXIT_COMMANDS=exit,quit,stop,goodbye,bye,exit misa
MAX_RETRIES=5
```

You can find available `voice_id`s by logging into ElevenLabs and checking your voice dashboard.

---

## 🚀 Usage

### Run the Assistant

```bash
python main.py
```

### Conversation Flow

1. The assistant will **listen** to your voice input via microphone.
2. The input is converted to text using Google Speech Recognition.
3. Gemini generates a **custom AI response** based on your conversation history and personality settings.
4. ElevenLabs converts the AI text into **spoken audio** and plays it.
5. The loop continues until you say any of the **exit commands** (e.g., "exit", "stop").

---

## 🔧 Customization Options

All customization is controlled via environment variables:

| Variable         | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `AI_NAME`        | Name of your assistant (used in printed and spoken text)      |
| `AI_PERSONALITY` | Prompt that defines your assistant’s personality and tone     |
| `VOICE_ID`       | ElevenLabs voice ID (e.g., Rachel, Bella, etc.)               |
| `MODEL_ID`       | ElevenLabs voice model ID (default: `eleven_multilingual_v2`) |
| `EXIT_COMMANDS`  | Comma-separated phrases to stop the assistant                 |
| `MAX_RETRIES`    | Number of retries for failed voice recognition attempts       |

---

## 🧠 How It Works

```plaintext
Your voice → [SpeechRecognition] → Text
          → [Google Gemini] → AI response (text)
          → [ElevenLabs] → Audio (MP3)
          → [Pygame] → Plays the voice
```

Conversation context is preserved to maintain continuity and sarcasm 😎.

---

## 🧪 Tips & Troubleshooting

* 🔇 **Microphone not working?** Make sure your default input device is enabled and accessible.
* 🔑 **API Key errors?** Double-check your `.env` keys and ensure the services are active.
* 🧠 **Want a polite assistant?** Just replace the `AI_PERSONALITY` with a friendly or formal description.

---

## 📁 Project Structure

```
├── main.py
├── .env
├── requirements.txt
```

---

## 📄 License

MIT License — feel free to use, fork, and personalize.

---

Would you like a sample `requirements.txt` or a quick-start `.env` template included in the repo?
