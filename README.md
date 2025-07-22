
# Jarvis - Voice Assistant using Python

Jarvis is a simple AI-powered voice assistant built with Python. It can:
- Open popular websites like Google, YouTube, Facebook
- Play songs from a predefined library
- Fetch top news headlines
- Answer any query using Google's Gemini AI
- Respond to your voice using Text-to-Speech

---

## Features

-  Speech Recognition (Google API)
-  Text-to-Speech (pyttsx3)
-  News fetching (NewsAPI)
-  Google Gemini AI Integration
-  Music Playback via Browser
-  Wake Word Activation: `Jarvis`

---

##  Tech Stack
- Python 3.11
- `speech_recognition` 
- `pyttsx3` 
- `pyaudio` 
- `requests` 
- `webbrowser` 
- `google.generativeai` (Gemini) 
- `NewsAPI` 

---

##  Project Structure
```
   jarvis
 ┣  main.py
 ┣  musicLibrary.py
 ┣  requirements.txt
 ┗  README.md
```

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/jarvis.git
cd jarvis
```

### 2. Setup Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment
Windows PowerShell:
```bash
.venv\Scripts\Activate.ps1
```

### 4. Install Requirements
```bash
pip install -r requirements.txt
```

---

##  Important Notes

-  **News API Key** — Replace the key in `main.py` → `newsapi = "<YOUR_API_KEY>"`
-  **Gemini API Key** — Replace with your Google Gemini API key in `main.py`
-  **musicLibrary.py** — Create a dictionary of songs like:
```python
music = {
    "songname": "https://link-to-song",
    "another": "https://another-link"
}
```
-  **PyAudio Fix** — Install with:
```bash
pip install pipwin
pipwin install pyaudio
```
Or download PyAudio wheel for Python 3.11 if pipwin fails.

---

##  How to Run
```bash
python main.py
```
Say “Jarvis” to activate. Ask to open websites, play music, get news, or ask any question!

---

##  Example Commands
- "Jarvis" → wake word
- "Open Google"
- "Play [songname]"
- "News"
- "Who is Elon Musk?"

---

##  Future Improvements
- Custom wake words
- Weather integration
- Reminder system
- Smarter conversational responses

---

## License
MIT License

---

##  Credits
Made with  by Hrishav Raj
