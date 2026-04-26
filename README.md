# ⚡ CodeCraft Pro — AI Code Review Tool

An AI-powered web application that reviews your HTML, CSS, and JavaScript code instantly.

## ✨ Features
- 🤖 AI code review using Groq's Llama3-8B model
- 👁️ Live preview — see rendered code alongside AI feedback
- ⚡ Instant analysis — mistakes, improvements, best practices
- 🎨 Beautiful dark-themed UI

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| AI Model | Groq API — Llama3-8B |
| Backend | Flask REST API |
| Frontend | HTML, CSS, JavaScript |

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Jiyarana19/codecraft-pro.git
```

### 2. Install dependencies
```bash
pip install flask flask-cors groq python-dotenv
```

### 3. Add API key
Create `.env` file in backend folder:
GROQ_API_KEY=your_groq_api_key_here

Get free API key at console.groq.com

### 4. Run backend
```bash
cd backend
python app.py
```

### 5. Open frontend
Open `frontend/index.html` in browser

## 📁 Project Structure
codecraft-pro/
├── backend/
│   ├── app.py           # Flask API
│   └── ai_feedback.py   # Groq AI integration
├── frontend/
│   ├── index.html       # Main UI
│   ├── style.css        # Styling
│   └── script.js        # Frontend logic
