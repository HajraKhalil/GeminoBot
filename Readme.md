# 🤖 Gemini-Powered Chatbot

A sleek, real-time AI chatbot built with **Flask** and integrated with **Gemini API**, featuring a clean UI and modern web tech. Type, talk, and get instant responses powered by Google's cutting-edge AI.

## 🚀 Features

- 💬 Real-time Gemini API responses
- 🔤 Modern UI with JavaScript, HTML5, and CSS3
- 🔒 Secure environment variable handling via `.env`
- 🌐 RESTful backend powered by Flask
- 📁 Structured project layout for scalability

## 📁 Project Structure

```
chatbot/
├── config/
│   └── .env
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── main.py
├── .gitignore
└── README.md
```

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/chatbot.git
   cd chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file** in the `config/` directory:
   ```
   GEMINI_API_KEY=your_key_here
   ```

5. **Run the Flask app**
   ```bash
   python main.py
   ```

## 🧬 Tech Stack

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI Integration:** Gemini API
- **Deployment-ready:** Easily hostable via Render, Vercel (frontend), or PythonAnywhere

## 📸 Demo

> Screenshots or video demos coming soon...

## 💡 Use Cases

- AI-driven customer support
- Conversational agents for websites
- Smart assistants for educational platforms

## 🛡️ Security

- `.env` file excluded using `.gitignore` to keep API keys safe
- Keys loaded securely using `python-dotenv`

## 🙌 Contributions

Feel free to fork and submit PRs. All ideas welcome!

## 📬 Contact

Message at khalilhajra5@gmail.com or connect via https://www.linkedin.com/in/hajra-khalil-84b08627b/

