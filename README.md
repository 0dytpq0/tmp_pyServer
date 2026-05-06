# tmp_pyServer

## 프로젝트 개요

Python 기반 서버 프로젝트입니다.

---

## 환경 설정 가이드

### 사전 요구사항

- **Python 3.11.8** (버전 일치 권장)

### 1. 가상환경 생성

```bash
python -m venv .venv
```

### 2. 가상환경 활성화

#### Windows

```powershell
# PowerShell
.\.venv\Scripts\Activate.ps1

# CMD
.\.venv\Scripts\activate.bat
```

> ⚠️ PowerShell에서 실행 정책 오류 발생 시 아래 명령을 **관리자 권한**으로 실행하세요:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### macOS / Linux

```bash
source .venv/bin/activate
```

활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 환경변수 설정

`.env.example` 파일을 복사하여 `.env` 파일을 생성한 뒤, 본인의 API 키를 입력하세요. (`.env`는 Git에 포함되지 않습니다)

#### Windows

```powershell
copy .env.example .env
```

#### macOS / Linux

```bash
cp .env.example .env
```

---

## 패키지 관리

### 새 패키지 추가 시

```bash
# 패키지 설치
pip install <패키지이름>

# requirements.txt 업데이트 (필수!)
pip freeze > requirements.txt
```

### 다른 팀원이 패키지를 추가한 경우

```bash
# pull 후 종속성 동기화
pip install -r requirements.txt
```

---

## 빠른 시작 (신규 팀원용)

### Windows

```powershell
git clone <저장소URL>
cd tmp_pyServer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS / Linux

```bash
git clone <저장소URL>
cd tmp_pyServer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
