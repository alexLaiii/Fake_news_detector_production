import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from predict import predict_fake_news

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app = FastAPI(title="Fake News Detector API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in ALLOWED_ORIGINS if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StatementInput(BaseModel):
    statement: str

@app.get("/")
def root():
    return {"ok": True, "message": "Fake News Detector API", "routes": ["/state", "/analyze"]}

@app.get("/state")
def state():
    return {"status": "running"}

@app.post("/analyze")
def analyze(inp: StatementInput):
    return predict_fake_news(inp.statement)
