import json
from google import genai
from google.genai import types
from config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_resume(text, role):
    prompt=f'''Analyze this resume for a {role} role. Return ONLY valid JSON with keys overall_score, summary, scores, strengths, weaknesses, missing_skills, top_recommendation. Resume: {text}'''
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(temperature=0),
            contents=prompt
        )
        raw=response.text.strip()
        start=raw.find('{'); end=raw.rfind('}')+1
        return json.loads(raw[start:end])
    except Exception as e:
        return {'error': str(e), 'scores': {}}