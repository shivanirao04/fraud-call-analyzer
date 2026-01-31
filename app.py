from fastapi import FastAPI, Query, Header
import whisper
import requests
import uuid
import os

app = FastAPI()
model = whisper.load_model("base")

FRAUD_KEYWORDS = [
    "otp", "one time password", "bank", "account blocked",
    "kyc", "urgent", "verify", "click", "transfer",
    "upi", "card", "pin"
]

@app.post("/analyze-call")
def analyze_call(
    audio_url: str = Query(...),
    authorization: str = Header(default=None)
):
    filename = f"audio_{uuid.uuid4()}.mp3"

    try:
        response = requests.get(audio_url, timeout=20)
        response.raise_for_status()

        with open(filename, "wb") as f:
            f.write(response.content)

        result = model.transcribe(filename)
        transcript = result.get("text", "").lower()

        risk_score = 0
        matched = []

        for word in FRAUD_KEYWORDS:
            if word in transcript:
                risk_score += 10
                matched.append(word)

        if risk_score >= 30:
            label = "FRAUD"
        elif risk_score >= 10:
            label = "SUSPICIOUS"
        else:
            label = "SAFE"

        return {
            "status": "success",
            "classification": label,
            "risk_score": risk_score,
            "matched_keywords": matched,
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
