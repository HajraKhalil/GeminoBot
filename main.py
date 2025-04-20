from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import traceback
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")

# Configure CORS for the /chat endpoint
CORS(app, resources={
    r"/chat": {
        "origins": ["http://localhost:8000", "http://127.0.0.1:8000"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Google Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"  
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"

# Serve the index.html page
@app.route("/")
def index():
    return render_template("index.html")

# Handle CORS preflight OPTIONS request and chat POST request
@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    # Validate incoming JSON data
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Please enter a message!"}), 400
    except Exception as e:
        print(f"Error parsing JSON: {str(e)}")
        return jsonify({"error": "Invalid JSON data", "details": str(e)}), 400

    # Prepare headers and payload for Gemini API
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 512
        }
    }

    try:
        # Make request to Gemini API
        print(f"Sending request to Gemini API with model: {MODEL_NAME}")
        response = requests.post(f"{API_URL}?key={GEMINI_API_KEY}", headers=headers, json=payload, timeout=10)
        response.raise_for_status()  # Raises an exception for 4xx/5xx errors

        response_data = response.json()
        print(f"API response: {response_data}")
        if not response_data.get("candidates"):
            return jsonify({"error": "Unexpected API response format", "details": "No candidates in response"}), 500

        # Extract and return the response
        chat_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"response": chat_response})

    except requests.exceptions.HTTPError as e:
        error_details = e.response.text if e.response else str(e)
        print(f"API request failed: {error_details}")
        print(f"Status code: {e.response.status_code if e.response else 'N/A'}")
        return jsonify({"error": "API request failed", "details": error_details}), 500
    except requests.exceptions.RequestException as e:
        print(f"Network error: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": "Network error", "details": str(e)}), 500
    except Exception as e:
        print(f"Internal server error: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)