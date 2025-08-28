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
    # One-shot prompt: provide an example summary, then a new task
    user_prompt = (
        "Summarize the following text in one sentence.\n"
        "Example:\n"
        "Text: The sun is the center of our solar system and provides the energy necessary for life on Earth.\n"
        "Summary: The sun is vital for life on Earth as the solar system's center.\n"
        "Now summarize this text:\n"
        "Text: Artificial Intelligence is transforming the world by enabling machines to learn from data and make decisions.\n"
        "Summary:"
    )