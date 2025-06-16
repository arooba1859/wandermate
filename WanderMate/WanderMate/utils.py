# utils.py

import requests
from config import API_KEY, MODEL

def get_chatbot_response(messages):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "https://your-app.com",
            "X-Title": "WanderMate"
        },
        json={
            "model": MODEL,
            "messages": messages,
            "temperature": 0.7
        }
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
