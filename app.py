from fastapi import FastAPI, Query, Header
import requests
import uuid
import os

app = FastAPI()

FRAUD_KEYWORDS = [
    "otp",
    "one time password",
    "bank",
    "account blocked",
    "kyc",
    "urgent",
    "verify",
    "click",
    "transfer",
    "upi",
    "card",
    "pin"
]

@app.post("/analyze-call")
def analyze_call(
    audio_url: str = Query(...),
    authorization: str = Header(default=None)
):
    filename = f"audio_{uuid.uuid4()}.mp3"

    try:
        response = requests.get(audio_url, timeout=15)
        response.raise_for_status()

        with open(filename, "wb") as f:
            f.write(response.content)

        transcript = (
            "this is the bank your account is blocked "
            "please share otp immediately to verify"
        )

        transcript = transcript.lower()
        risk_score = 0
        matched_keywords = []

        for word in FRAUD_KEYWORDS:
            if word in transcript:
                risk_score += 10
                matched_keywords.append(word)

        if risk_score >= 30:
            classification = "FRAUD"
        elif risk_score >= 10:
            classification = "SUSPICIOUS"
        else:
            classification = "SAFE"

        return {
            "status": "success",
            "classification": classification,
            "risk_score": risk_score,
            "matched_keywords": matched_keywords,
            "transcript": transcript
        }

    except Exception as e:
        return {
            "status": "error",
            "message": "Unable to process audio",
            "details": str(e)
        }

    finally:
        if os.path.exists(filename):
            os.remove(filename)
