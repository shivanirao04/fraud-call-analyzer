from fastapi import FastAPI, Header
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

FRAUD_KEYWORDS = [
    "otp", "bank", "account blocked", "kyc",
    "urgent", "verify", "click", "upi", "pin"
]

class AnalyzeRequest(BaseModel):
    language: str
    audio_format: str = Field(..., alias="audioFormat")
    audio_base64: str = Field(..., alias="audioBase64")

    class Config:
        allow_population_by_field_name = True

@app.post("/analyze-call")
def analyze_call(
    request: AnalyzeRequest,
    x_api_key: Optional[str] = Header(None)
):
    transcript = "this is the bank your account is blocked please share otp"

    transcript = transcript.lower()
    risk_score = 0
    matched_keywords = []

    for word in FRAUD_KEYWORDS:
        if word in transcript:
            risk_score += 10
            matched_keywords.append(word)

    classification = (
        "FRAUD" if risk_score >= 30
        else "SUSPICIOUS" if risk_score >= 10
        else "SAFE"
    )

    return {
        "status": "success",
        "classification": classification,
        "risk_score": risk_score,
        "matched_keywords": matched_keywords,
        "message": "Potential fraud detected based on keyword patterns"
    }

@app.get("/")
def root():
    return {"message": "API is running"}
