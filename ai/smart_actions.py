import os
from ai.ai_selector import AISelector

AI_ENABLED = os.getenv("AI_ENABLED", "false").lower() == "true"


def smart_click(page, description, fallback):
    # 1️⃣ First try normal selector
    try:
        page.click(fallback)
        return
    except Exception as e:
        print(f"[WARN] Fallback click failed: {fallback} | {e}")

    # 2️⃣ Try AI only if enabled
    if AI_ENABLED:
        try:
            sel = AISelector.find(page, description)
            if sel and sel != "NOT_FOUND":
                page.click(sel)
                print(f"[AI] Click healed using selector: {sel}")
                return
        except Exception as e:
            print(f"[AI ERROR] smart_click failed: {e}")

    # 3️⃣ Hard fail
    raise Exception(
        f"smart_click failed. Description='{description}', fallback='{fallback}'"
    )


def smart_fill(page, description, fallback, value):
    # 1️⃣ First try normal selector
    try:
        page.fill(fallback, value)
        return
    except Exception as e:
        print(f"[WARN] Fallback fill failed: {fallback} | {e}")

    # 2️⃣ Try AI only if enabled
    if AI_ENABLED:
        try:
            sel = AISelector.find(page, description)
            if sel and sel != "NOT_FOUND":
                page.fill(sel, value)
                print(f"[AI] Fill healed using selector: {sel}")
                return
        except Exception as e:
            print(f"[AI ERROR] smart_fill failed: {e}")

    # 3️⃣ Hard fail
    raise Exception(
        f"smart_fill failed. Description='{description}', fallback='{fallback}'"
    )
