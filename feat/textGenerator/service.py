import json
from .config import client, MODEL
from .prompts import SUMMARY_PROMPT, SCRIPT_PROMPT
from .utils import safe_json_load

def call_gemini(prompt):
    res = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return res.text

def summarize(article):
    result = call_gemini(SUMMARY_PROMPT.format(article=article))
    return safe_json_load(result)

def generate_script(summary_json):
    prompt = SCRIPT_PROMPT.format(
        data=json.dumps(summary_json, ensure_ascii=False)
    )
    return call_gemini(prompt)

def generate(article):
    summary = summarize(article)
    return generate_script(summary)