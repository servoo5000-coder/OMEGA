from uuid import uuid4
from typing import Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field


APP_NAME = "OMEGA"
APP_VERSION = "0.1.0"

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="OMEGA analysis engine",
)

# السماح لواجهة Android WebView بالاتصال بالخادم
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
    mode: Literal["general", "technical", "scientific"] = "general"
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
        return {
            "status": "invalid_input",
            "message": "Input is empty",
        }

    steps = [
        "تحديد الهدف والسؤال الأساسي",
        "تقسيم المشكلة إلى عناصر أصغر",
        "تحديد المعلومات المتاحة والناقصة",
        "صياغة فرضيات قابلة للاختبار",
        "اقتراح تجربة للتحقق",
        "مراجعة النتائج والقيود",
        "استخلاص ما يمكن استنتاجه",
    ]

    selected_steps = steps[:request.max_steps]

    return {
        "engine": APP_NAME,
        "version": APP_VERSION,
        "request_id": uuid4().hex,
        "status": "rules_fallback",
        "mode": request.mode,
        "objective": subject,
        "plan": {
            "steps": selected_steps,
        },
        "hypotheses": [
            {
                "statement": (
                    "توجد احتمالات متعددة تحتاج إلى "
                    "معلومات إضافية للتحقق منها."
                ),
                "status": "untested",
                "confidence": None,
                "evidence_needed": [
                    "بيانات موثوقة",
                    "اختبار قابل للتكرار",
                    "مقارنة النتائج",
                ],
            }
        ],
        "critique": {
            "limitations": [
                "التحليل الحالي يعتمد على قواعد محلية.",
                "لم يتم إجراء تجربة واقعية.",
                "لم يتم التحقق من الفرضيات بمصادر خارجية.",
            ],
            "conclusion": "نتائج أولية وليست حقائق مثبتة.",
        },
        "storage": {
            "persistent": False,
            "session_only": True,
        },
}
