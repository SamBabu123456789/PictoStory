import requests

API_KEY = "AIzaSyDIZukfnO2QBnGwHnyebJbSRVnitlxnI3Y"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def ask_gemini(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    # Zero-shot prompt: ask Gemini to summarize text
    user_prompt = "Summarize the following text in one sentence: Artificial Intelligence is transforming the world by enabling machines to learn from data and make decisions."
    result = ask_gemini(user_prompt)
    print(result)