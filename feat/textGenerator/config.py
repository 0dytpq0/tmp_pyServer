import os
from functools import lru_cache
from dotenv import load_dotenv
from google import genai

load_dotenv()

# 모델명은 환경변수로 덮어쓸 수 있게 두고, 기본값은 현재 사용 모델로 고정한다.
MODEL = os.getenv("GENAI_MODEL", "gemini-3-flash-preview")


def get_api_key():
    # import 시점이 아니라 실제 호출 시점에 API 키 누락을 검증한다.
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise RuntimeError("GENAI_API_KEY 환경변수가 설정되어 있지 않습니다.")
    return api_key


@lru_cache
def get_client():
    # Gemini 클라이언트는 생성 비용이 있으므로 프로세스 안에서 재사용한다.
    return genai.Client(api_key=get_api_key())
