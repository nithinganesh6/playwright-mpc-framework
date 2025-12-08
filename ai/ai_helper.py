import os
import requests


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_BASE = os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1')
AI_ENABLED = os.getenv('AI_ENABLED', 'false').lower() == 'true'




def call_llm(prompt: str):
    if not AI_ENABLED or not OPENAI_API_KEY:
      raise RuntimeError('AI not enabled or OPENAI_API_KEY missing')


    url = f"{OPENAI_API_BASE}/chat/completions"
    headers = {
      'Authorization': f'Bearer {OPENAI_API_KEY}',
      'Content-Type': 'application/json'
    }
    payload = {
      'model': 'gpt-4o-mini',
      'messages': [{'role': 'user', 'content': prompt}],
      'temperature': 0.0
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data['choices'][0]['message']['content']