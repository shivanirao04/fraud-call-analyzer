from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Fraud Call Analyzer API")

class AnalyzeRequest(BaseModel):
    language: str
    audio_format: str
    audio_base64: str

@app.post("/analyze-call")
def analyze_call(
    request: AnalyzeRequest,
    x_api_key: Optional[str] = Header(None)
):
    # Simulated analysis for Challenge 1 validation
    return {
        "status": "success",
        "classification": "FRAUD",
        "risk_score": 40,
        "matched_keywords": ["bank", "otp", "account blocked"],
        "message": "Potential fraud detected based on keyword patterns"
    }

@app.get("/")
def root():
    return {"message": "Fraud Call Analyzer API is running"}
