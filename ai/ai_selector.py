from playwright.sync_api import Page
from .ai_helper import call_llm


class AISelector:
    @staticmethod
    def find(page: Page, description: str) -> str:
        html = page.content()
        prompt = f"""
        You are an assistant that provides a single robust CSS selector for the described element.
        Description: {description}


HTML:
{html}


Return a single CSS selector or NOT_FOUND.
"""
        candidate = call_llm(prompt)
        if not candidate:
            return 'NOT_FOUND'
        return candidate.strip().replace('\n', ' ')