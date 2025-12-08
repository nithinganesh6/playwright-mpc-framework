from .ai_helper import call_llm




def generate_steps_from_nl(nl: str) -> str:
    prompt = f"Convert this test case into a JSON array of simple steps for Playwright (actions: goto, click, fill, expect_url, expect_text).\n\n{nl}\n"
    return call_llm(prompt)