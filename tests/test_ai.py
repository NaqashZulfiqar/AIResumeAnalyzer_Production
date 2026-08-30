from services.ai_service import analyze_resume

def test_result_is_dict():
    r=analyze_resume('Python ML developer','AI/ML Engineer')
    assert isinstance(r, dict)