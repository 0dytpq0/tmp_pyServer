import os
import json
import re
from dotenv import load_dotenv
from google import genai

# 🔹 환경 설정
load_dotenv()
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
MODEL = "gemini-3-flash-preview"

# 🔹 공통 함수
def call_gemini(prompt):
    res = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return res.text

def clean_json(text):
    return re.sub(r"```json|```", "", text).strip()

# 🔹 캐릭터 & 스타일
CHARACTER = "20대 남성, 검은 머리, 안경, 캐주얼 복장"
STYLE = "일본 애니메이션 스타일, 감성적인 조명, 부드러운 색감"

#  1. 대본 → 장면 분해
"""
아마 대본자체에 Scean을 나눠놓고 이를 json형식에 추가해서 전달하는게 옳다고 봄
아래는 그냥 테스트용
"""
def split_into_scenes(script):
    prompt = f"""
다음 대본을 6~9개의 장면으로 나눠라.

조건:
- JSON 배열만 출력
- 각 요소는 desc 포함

형식:
[
  {{"desc": ""}}
]

대본:
{script}
"""
    result = call_gemini(prompt)

    try:
        return json.loads(clean_json(result))
    except:
        print("❌ JSON 파싱 실패:", result)
        return []

# 2. 이미지 프롬프트 생성
"""
캐릭터, 이미지 스타일 또한 웹에서 클릭을 하든 어떤 스타일을 불변값으로 지정해놓는 것이 좋아보임
이는 여러 이미지를 전달해주고 그 프롬프트를 불변값으로 저장해놓을 것
"""
def make_image_prompt(scene_desc):
    return f"""
same character, consistent face, same outfit

{CHARACTER}

{STYLE}

장면:
{scene_desc}

cinematic shot, detailed, high quality
"""

# 🔥 3. 이미지 생성 (현재는 테스트용)
def generate_image(prompt):
    print("\n🖼️ 생성 프롬프트:\n", prompt)
    return "dummy_image.png"
# api연결시
# def generate_image(prompt, index=0):
#     import os
#     os.makedirs("outputs", exist_ok=True)

#     try:
#         response = client.models.generate_content(
#             model="gemini-3.1-flash-image-preview",
#             contents=[prompt],
#         )
         #현재 image를 outputs 폴더를 만들어 저장하는 방식인데, 실제론 s3에 올려야할거같음 => 방법구해보기

#         for part in response.candidates[0].content.parts:
#             if part.inline_data is not None:
#                 image = part.as_image()
#                 filename = f"outputs/scene_{index}.png"
#                 image.save(filename)
#                 return filename

#     except Exception as e:
#         print("❌ 이미지 생성 실패:", e)
#         return None


# 🔥 4. 전체 흐름
def generate_images_from_script(script):
    scenes = split_into_scenes(script)

    images = []

    for i, scene in enumerate(scenes):
        prompt = make_image_prompt(scene["desc"])
        img = generate_image(prompt)
        images.append(img)

    return images

# 🔥 실행 테스트
if __name__ == "__main__":
    script = """
    이거 진짜 충격입니다.
    한 회사가 갑자기 무너졌습니다.
    내부 문제가 있었고 결국 파산했습니다.
    """
    result = generate_images_from_script(script)
    print("\n최종 결과:", result)