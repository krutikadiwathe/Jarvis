
# 🤖 Optimus – A Voice-Activated Desktop Assistant

**Optimus** is a personal voice assistant built in Python that responds to natural language commands. It can play music, fetch jokes, search Wikipedia, open websites, launch applications, and even shut down when asked — all through your voice.

This project showcases real-time voice interaction, API integration, and automation using Python.

---

## 🎯 Features

- 🎵 Play or pause your Spotify playlist via Spotipy
- 📚 Search and summarize topics from Wikipedia
- 😂 Tell random dad jokes via icanhazdadjoke API
- 🌐 Open popular websites (YouTube, Google, LinkedIn, Stack Overflow)
- 💻 Launch local applications like Visual Studio Code
- 🕒 Speak the current system time
- 🛑 Gracefully shuts down on voice command (“stop”, “exit”, “quit”)

---

## 🎥 Demo Video

📽️ [Watch the full walkthrough here] https://www.linkedin.com/feed/update/urn:li:ugcPost:7338420757510713344/

---

## 🧰 Tech Stack

- Python 3.12+
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – for voice command capture
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – for text-to-speech responses
- [`spotipy`](https://spotipy.readthedocs.io/) – to control Spotify playback
- [`wikipedia`](https://pypi.org/project/wikipedia/) – for summarizing search results
- [`requests`](https://pypi.org/project/requests/) – for calling APIs like jokes
- `os`, `subprocess`, and `webbrowser` – for system and web interactions

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/optimus-voice-assistant.git
cd optimus-voice-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your Spotify Credentials

Replace in your script:

```python
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'http://127.0.0.1:8888/callback'
```

> 🎧 You’ll need a Spotify developer account and active device

### 4. Run the Assistant

```bash
python jarvis.py
```

---

## 🗣 Example Voice Commands

| 🗨️ Command                  | 💡 Action                            |
|----------------------------|--------------------------------------|
| "Play music"               | Starts playing your Spotify playlist |
| "Pause music"              | Pauses Spotify playback              |
| "Tell me a joke"           | Tells a random dad joke              |
| "Search Wikipedia for AI"  | Reads a summary about AI             |
| "Open Google"              | Opens google.com in browser          |
| "What time is it?"         | Speaks current system time           |
| "Stop" / "Exit" / "Quit"   | Gracefully shuts down Optimus        |

---

## 📌 Notes

- Requires a working microphone and internet connection
- Spotify app must be running and linked to your account
- Built and tested on Windows 10 with Python 3.12

---

## 👩‍💻 Author

**Krutika Diwathe**  
M.S. in Computer Science | AI & Automation Enthusiast  
📍 Cleveland State University  
🔗 [LinkedIn](https://www.linkedin.com/in/krutika-diwathe)

---

## 📎 License

This project is licensed under the MIT License.

---

> 💡 *Built with Python and curiosity — to make everyday tasks hands-free and smart.*
