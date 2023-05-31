import os

import requests

OPENAI_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.environ["GPT_API"]


def create_payload(
    model_name: str, prompt_message: str, temperature: float = 0.2, top_n: float = 0
) -> dict:
    payload = {
        "model": model_name,
        "messages": [{"role": "system", "content": prompt_message}],
        "temperature": temperature,
        "top_p": top_n,
    }
    return payload


def hit_api(payload: dict) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    response = requests.post(url=OPENAI_URL, headers=headers, json=payload)
    output = response.json()
    return output


msg = "who was hamlet"
pay = create_payload(model_name="gpt-3.5-turbo", prompt_message=msg)
api_output = hit_api(pay)
