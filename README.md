# tmp_pyServer

## 프로젝트 개요

Python 기반 서버 프로젝트입니다.

---

## 환경 설정 가이드

### 사전 요구사항

- **uv**
- **Python 3.13** (`.python-version` 기준)

uv가 설치되어 있지 않다면 먼저 설치하세요.

```powershell
winget install --id astral-sh.uv
```

macOS / Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 1. 의존성 동기화

프로젝트는 `pyproject.toml`과 `uv.lock`을 기준으로 의존성을 관리합니다.

```bash
uv sync
```

`uv sync`는 필요한 경우 `.venv`를 자동으로 생성하고, `uv.lock`에 고정된 버전으로 패키지를 설치합니다. 별도로 `python -m venv`나 `pip install -r requirements.txt`를 실행할 필요가 없습니다.

### 2. 환경변수 설정

`.env.example` 파일을 복사하여 `.env` 파일을 생성한 뒤, 본인의 API 키를 입력하세요. (`.env`는 Git에 포함되지 않습니다)

Windows:

```powershell
copy .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

### 3. 실행

가상환경을 직접 활성화하지 않고 `uv run`으로 실행합니다.

```bash
uv run python main.py
```

텍스트 생성 모듈 실행:

```bash
uv run python -m feat.textGenerator.main
```

이미지 생성 모듈 실행:

```bash
uv run python -m feat.imageGenerator.main
```

---

## 패키지 관리

### 새 패키지 추가

```bash
uv add <패키지이름>
```

개발용 패키지 추가:

```bash
uv add --dev <패키지이름>
```

### 패키지 제거

```bash
uv remove <패키지이름>
```

### 다른 팀원이 패키지를 추가한 경우

```bash
git pull
uv sync
```

### 의존성 확인

```bash
uv tree
```

---

## 기존 팀원 업데이트 가이드

이미 프로젝트를 클론해서 작업 중인 팀원은 작업 중인 변경사항을 먼저 확인한 뒤 최신 변경사항을 받습니다.

```bash
git status
```

작업 중인 파일이 있다면 커밋하거나 임시 저장한 뒤 업데이트하세요.

```bash
git pull
uv sync
```

`uv sync`는 `pyproject.toml`과 `uv.lock` 변경사항을 기준으로 `.venv`를 자동 업데이트합니다. 새 패키지가 추가되었거나 버전이 바뀐 경우에도 별도 `pip install` 없이 이 명령만 실행하면 됩니다.

### 업데이트 후 확인할 것

```bash
uv run python main.py
```

텍스트 생성 모듈을 확인하려면 아래 명령을 실행합니다.

```bash
uv run python -m feat.textGenerator.main
```

### 환경변수가 추가된 경우

팀원이 `.env.example`에 새 환경변수를 추가했을 수 있습니다. pull 이후 `.env.example` 변경사항을 확인하고, 필요한 값이 있으면 본인의 `.env`에 직접 추가하세요.

```bash
git diff ORIG_HEAD -- .env.example
```

의존성 변경사항까지 함께 확인하려면 아래처럼 실행합니다.

```bash
git diff ORIG_HEAD -- pyproject.toml uv.lock .env.example
```

### 의존성 파일 충돌이 난 경우

`pyproject.toml` 또는 `uv.lock`에서 충돌이 발생하면 충돌을 해결한 뒤 lock 파일을 다시 갱신합니다.

```bash
uv lock
uv sync
```

> 의존성은 `requirements.txt`가 아니라 `pyproject.toml`과 `uv.lock` 기준으로 관리합니다. 새 패키지를 설치할 때는 `pip install` 대신 `uv add <패키지이름>`을 사용하세요.

---

## 빠른 시작 (신규 팀원용)

### Windows

```powershell
git clone <저장소URL>
cd tmp_pyServer
uv sync
copy .env.example .env
uv run python main.py
```

### macOS / Linux

```bash
git clone <저장소URL>
cd tmp_pyServer
uv sync
cp .env.example .env
uv run python main.py
```

---

## 주요 파일

| 파일 | 역할 |
|------|------|
| `pyproject.toml` | 프로젝트 메타데이터와 의존성 선언 |
| `uv.lock` | 정확한 의존성 버전 고정 |
| `.python-version` | 프로젝트 Python 버전 |
| `.env.example` | 필요한 환경변수 예시 |
| `feat/textGenerator/` | 기사 요약 및 쇼츠 대본 생성 |
| `feat/imageGenerator/` | 이미지 프롬프트 및 이미지 생성 흐름 |

> `requirements.txt`는 기존 pip 방식의 잔여 파일입니다. 새 의존성 관리는 `uv add`와 `pyproject.toml` 기준으로 진행하세요.
