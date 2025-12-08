import os
from ai.ai_selector import AISelector

def smart_click(page, description, fallback):
    if os.getenv("AI_ENABLED", "false").lower() == "true":
        sel = AISelector.find(page, description)
        if sel != "NOT_FOUND":
            try:
                page.click(sel)
                return
            except:
                pass
    page.click(fallback)


def smart_fill(page, description, fallback, value):
    if os.getenv("AI_ENABLED", "false").lower() == "true":
        sel = AISelector.find(page, description)
        if sel != "NOT_FOUND":
            try:
                page.fill(sel, value)
                return
            except:
                pass
    page.fill(fallback, value)
