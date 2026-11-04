

from uuid import uuid4
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field

from local_engine import (
    build_plan,
    generate_hypotheses,
    review_analysis,
)

APP_NAME = "OMEGA"
APP_VERSION = "0.2.0"

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="OMEGA Intelligence & Discovery Engine",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://appassets.androidplatform.net",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class AnalyzeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str = Field(min_length=1, max_length=4000)
    mode: Literal[
        "general",
        "technical",
        "scientific",
    ] = "general"
    max_steps: int = Field(default=5, ge=1, le=7)


@app.get("/health")
async def health():
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "status": "ready",
        "storage": "disabled",
    }


@app.post("/api/analyze")
async def analyze(request: AnalyzeRequest):
    subject = request.text.strip()

    if not subject:
        raise HTTPException(
            status_code=422,
            detail="Input cannot be empty",
        )

    try:
        # 1. Planning
        plan = build_plan(
            subject,
            max_steps=request.max_steps,
            mode=request.mode,
        )

        # 2. Hypothesis generation
        hypotheses = generate_hypotheses(subject)

        # 3. Critical review
        critique = review_analysis(
            subject,
            hypotheses,
        )

        # 4. Final response
        return {
            "engine": APP_NAME,
            "version": APP_VERSION,
            "request_id": uuid4().hex,
            "status": "rules_fallback",
            "mode": request.mode,
            "objective": subject,
            "plan": plan,
            "hypotheses": hypotheses,
            "critique": critique,
            "storage": {
                "persistent": False,
                "session_only": True,
            },
        }

    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="OMEGA analysis engine error",
        )
