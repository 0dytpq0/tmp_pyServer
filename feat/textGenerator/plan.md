# feat/textGenerator 기능 명세

## Summary

`feat/textGenerator`는 기사 본문을 입력받아 LLM으로 요약하고, 그 요약을 기반으로 유튜브 쇼츠 대본을 생성하는 기능이다.  
이번 단계의 목표는 구현을 확장하기 전에 LLM 로직의 책임과 흐름을 명확히 나누는 것이다.

## 핵심 기능

### 1. 기사 요약 기능

입력:

```python
article: str
```

처리:

- 기사 본문을 LLM 요약 프롬프트에 넣는다.
- LLM은 기사 핵심 정보를 JSON 형태로 반환해야 한다.
- JSON 코드블록이 포함되어도 파싱 가능해야 한다.

출력:

```python
{
  "title": "",
  "summary": "",
  "key_points": [],
  "tone": ""
}
```

### 2. 쇼츠 대본 생성 기능

입력:

```python
summary: dict
```

처리:

- 요약 결과를 기반으로 쇼츠 대본 프롬프트를 생성한다.
- 30~40초 분량의 대본을 생성한다.
- 초반 훅, 본문, 마무리 구조를 유지한다.

출력:

```text
[HOOK]
...

[BODY]
...

[ENDING]
...
```

### 3. 전체 생성 기능

입력:

```python
article: str
```

처리 흐름:

```text
기사 본문
-> 기사 요약 프롬프트 생성
-> LLM 요약 요청
-> 요약 응답 파싱
-> 대본 생성 프롬프트 생성
-> LLM 대본 요청
-> 최종 결과 반환
```

출력:

```python
{
  "summary": {
    "title": "",
    "summary": "",
    "key_points": [],
    "tone": ""
  },
  "script": ""
}
```

## 로직 분리 기준

### config

역할:

- 환경변수 관리
- Gemini API key 확인
- 모델명 관리
- Gemini client 생성

### llm

역할:

- LLM API 호출 전담
- prompt 검증
- 빈 응답 처리

### prompts

역할:

- 요약 프롬프트 생성
- 대본 프롬프트 생성
- 프롬프트 문구 관리

### parser

역할:

- LLM 응답 정리
- JSON 코드블록 제거
- JSON 파싱
- 파싱 실패 시 fallback 처리

### service

역할:

- 전체 기능 흐름 조립
- `summarize`
- `generate_script`
- `generate`

## 제외 범위

이번 명세에서는 아래 기능을 포함하지 않는다.

- URL 크롤링
- 이미지 생성
- DB 저장
- API 서버 라우팅
- 프론트엔드 연동
- 테스트 코드 확장

## 성공 기준

- 기사 본문 문자열만으로 요약과 대본 생성 흐름이 명확하다.
- LLM 호출 로직과 서비스 로직이 분리된다.
- 프롬프트 수정이 service 코드에 영향을 최소화한다.
- 최종 결과는 단순 문자열이 아니라 `summary`, `script`를 포함한 구조화된 dict로 반환된다.
- API key가 없을 때 import 단계가 아니라 실행 단계에서 명확한 에러가 발생한다.

## Assumptions

- 대상 폴더는 `feat/textGenerator`이다.
- 현재 단계는 구현이 아니라 기능 명세 수립 단계이다.
- 입력은 URL이 아닌 기사 본문 문자열이다.
- 우선순위는 테스트 코드보다 실제 LLM 처리 로직 설계이다.
