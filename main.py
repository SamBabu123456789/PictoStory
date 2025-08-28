import requests
import re
import json

API_KEY = "AIzaSyDIZukfnO2QBnGwHnyebJbSRVnitlxnI3Y"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def count_tokens(text):
    # Simple token count: split on whitespace and punctuation
    tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
    return len(tokens)

def ask_gemini(prompt, top_p=0.8, temperature=0.7, top_k=40):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ],
        "generationConfig": {
            "topP": top_p,
            "temperature": temperature,
            "topK": top_k
        }
    }
    response = requests.post(API_URL, headers=headers, json=data)
    result = response.json()
    # Count tokens in prompt and response
    prompt_tokens = count_tokens(prompt)
    # Try to extract response text
    try:
        response_text = result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        response_text = ""
    response_tokens = count_tokens(response_text)
    print(f"Prompt tokens: {prompt_tokens}, Response tokens: {response_tokens}, Total: {prompt_tokens + response_tokens}")
    return response_text

if __name__ == "__main__":
    # Dynamic prompting: build prompt based on user input
    task = input("What do you want to do? (summarize/translate): ").strip().lower()
    text = input("Enter the text: ").strip()

    if task == "summarize":
        user_prompt = (
            f"Summarize the following text in one sentence and return the result as JSON with a 'summary' key. "
            f"Text: {text}"
        )
    elif task == "translate":
        lang = input("Translate to which language?: ").strip()
        user_prompt = (
            f"Translate the following text to {lang} and return the result as JSON with a 'translation' key. "
            f"Text: {text}"
        )
    else:
        user_prompt = text  # fallback: just send the text

    # Set Top P, Temperature, and Top K values for generation
    response_text = ask_gemini(user_prompt, top_p=0.8, temperature=0.7, top_k=40)
    print("Raw model output:", response_text)
    # Try to parse structured output
    try:
        structured = json.loads(response_text)
        print("Structured output:", structured)
    except Exception:
        print("Could not parse structured output.")