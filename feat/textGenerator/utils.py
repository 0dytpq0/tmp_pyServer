import re
import json

def clean_json(text):
    return re.sub(r"```json|```", "", text).strip()

def safe_json_load(text):
    try:
        return json.loads(clean_json(text))
    except:
        return {"summary": text}