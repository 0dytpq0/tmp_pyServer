import re
import json

# Gemini가 JSON을 마크다운 코드블록으로 감싸서 돌려주는 경우를 정리한다.
JSON_FENCE_PATTERN = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$", re.IGNORECASE)


def clean_json(text):
    return JSON_FENCE_PATTERN.sub("", text).strip()


def safe_json_load(text):
    try:
        data = json.loads(clean_json(text))
    except json.JSONDecodeError:
        # JSON 파싱 실패 시에도 이후 대본 생성 단계가 받을 수 있는 dict 형태로 감싼다.
        return {"summary": text}

    if isinstance(data, dict):
        return data

    # 배열/문자열 같은 JSON도 프롬프트 입력 형식을 맞추기 위해 summary에 담는다.
    return {"summary": data}
