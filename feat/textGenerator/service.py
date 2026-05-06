import json
from .config import MODEL, get_client
from .prompts import SUMMARY_PROMPT, SCRIPT_PROMPT
from .utils import safe_json_load


# model에 prompt(답변)를 넣고 결과를 반환하는 함수
def call_gemini(prompt, gemini_client=None, model=MODEL):
    # 빈 프롬프트는 Gemini 호출 전에 차단해서 원인을 명확하게 만든다.
    if not prompt or not prompt.strip():
        raise ValueError("prompt는 비어 있을 수 없습니다.")

    # 테스트에서는 fake client를 주입하고, 실제 실행에서는 설정된 Gemini client를 사용한다.
    active_client = gemini_client or get_client()
    res = active_client.models.generate_content(model=model, contents=prompt)
    text = getattr(res, "text", None)

    # API 응답 객체가 있어도 본문이 비어 있으면 실패로 처리한다.
    if not text:
        raise RuntimeError("Gemini 응답이 비어 있습니다.")

    return text


# article을 받아서 요약하는 함수
def summarize(article, gemini_client=None):
    # 본문이 없는 상태에서 요약 프롬프트를 만들지 않도록 방어한다.
    if not article or not article.strip():
        raise ValueError("article은 비어 있을 수 없습니다.")

    result = call_gemini(
        SUMMARY_PROMPT.format(article=article.strip()),
        gemini_client=gemini_client,
    )
    return safe_json_load(result)


# 요약된 결과를 받아서 script를 생성하는 함수
def generate_script(summary_json, gemini_client=None):
    # 요약 결과가 없으면 대본 생성 프롬프트의 입력도 성립하지 않는다.
    if not summary_json:
        raise ValueError("summary_json은 비어 있을 수 없습니다.")

    prompt = SCRIPT_PROMPT.format(data=json.dumps(summary_json, ensure_ascii=False))
    return call_gemini(prompt, gemini_client=gemini_client)


# article을 받아서 generate_script까지 하는 함수
def generate(article):
    # 한 번의 생성 흐름에서는 같은 클라이언트를 재사용한다.
    gemini_client = get_client()
    summary = summarize(article, gemini_client=gemini_client)
    return generate_script(summary, gemini_client=gemini_client)
