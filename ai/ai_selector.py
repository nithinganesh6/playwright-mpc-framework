from ai.ai_helper import call_llm

# In-memory cache (per test run / per worker)
_SELECTOR_CACHE = {}


def _cache_key(page, description: str) -> str:
    try:
        url = page.url.split("?")[0]  # ignore query params
    except:
        url = "unknown"
    return f"{url}::{description.lower()}"


class AISelector:

    @staticmethod
    def find(page, description: str):
        key = _cache_key(page, description)

        # 1️⃣ Return cached selector if exists
        if key in _SELECTOR_CACHE:
            print(f"[AI CACHE] Using cached selector for '{description}'")
            return _SELECTOR_CACHE[key]

        # 2️⃣ Ask AI
        prompt = f"""
You are an expert Playwright test engineer.

Given the following HTML page, return the BEST Playwright selector
for the element described below.

Description: "{description}"

Return ONLY the selector. No explanation.
"""
        selector = call_llm(prompt)

        # 3️⃣ Cache result (even NOT_FOUND to avoid repeated calls)
        _SELECTOR_CACHE[key] = selector

        return selector
