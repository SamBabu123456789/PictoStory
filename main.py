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
    # Dynamic prompting: build prompt based on user input
    task = input("What do you want to do? (summarize/translate): ").strip().lower()
    text = input("Enter the text: ").strip()

    if task == "summarize":
        user_prompt = f"Summarize the following text in one sentence: {text}"
    elif task == "translate":
        lang = input("Translate to which language?: ").strip()
        user_prompt = f"Translate the following text to {lang}: {text}"
    else:
        user_prompt = text  # fallback: just send the text

    result = ask_gemini(user_prompt)
    print(result)