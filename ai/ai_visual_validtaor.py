from .ai_helper import call_llm

def compare_images_semantic(img_a_b64: str, img_b_b64: str) -> str:
    prompt = "Compare two screenshots (base64). Describe semantic differences and whether they are acceptable."
    return call_llm(prompt + "\n\nIMG_A:" + img_a_b64 + "\n\nIMG_B:" + img_b_b64)