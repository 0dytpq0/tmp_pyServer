import json
from .config import client, MODEL
from .prompts import SUMMARY_PROMPT, SCRIPT_PROMPT
from .utils import safe_json_load


# model에 prompt(답변)를 넣고 결과를 반환하는 함수
def call_gemini(prompt):
    res = client.models.generate_content(model=MODEL, contents=prompt)
    return res.text


# article을 받아서 요약하는 함수
def summarize(article):
    result = call_gemini(SUMMARY_PROMPT.format(article=article))
    return safe_json_load(result)


# 요약된 결과를 받아서 script를 생성하는 함수
def generate_script(summary_json):
    prompt = SCRIPT_PROMPT.format(data=json.dumps(summary_json, ensure_ascii=False))
    return call_gemini(prompt)


# article을 받아서 generate_script까지 하는 함수
def generate(article):
    summary = summarize(article)
    return generate_script(summary)
