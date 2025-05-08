
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Google Gemini API key here
GOOGLE_API_KEY = "AIzaSyAtF-LBFR026mNxMrUyzhAzqUdtQNSp6bg"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    personality = data.get('personality', 'friendly')

    # Define response prefixes based on personality
    if personality == "professional":
        prefix = "As a professional assistant, here's what I suggest: "
    elif personality == "funny":
        prefix = "Haha, good one! Anyway... "
    else:  # friendly
        prefix = "Sure buddy, here’s something that might help: "

    try:
        # Send message to Gemini API
        response = model.generate_content(message)
        final_response = f"{prefix}{response.text}"
        return jsonify({'response': final_response})
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)