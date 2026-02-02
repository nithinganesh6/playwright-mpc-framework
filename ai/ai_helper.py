import os
import requests

AI_ENABLED = os.getenv("AI_ENABLED", "false").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

AI_MAX_CALLS = int(os.getenv("AI_MAX_CALLS", "100"))
_AI_CALL_COUNT = 0


def _can_call_ai():
    global _AI_CALL_COUNT
    if _AI_CALL_COUNT >= AI_MAX_CALLS:
        print(f"[AI] Call limit reached ({_AI_CALL_COUNT}/{AI_MAX_CALLS})")
        return False
    _AI_CALL_COUNT += 1
    return True


def call_llm(prompt: str):
    # AI disabled → no call
    if not AI_ENABLED or not OPENAI_API_KEY:
        return "NOT_FOUND"

    # Hard safety limit
    if not _can_call_ai():
        return "NOT_FOUND"

    try:
        url = f"{OPENAI_API_BASE}/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"[AI ERROR] OpenAI call failed: {e}")
        return "NOT_FOUND"
