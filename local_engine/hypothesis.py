from typing import Any


def generate_hypotheses(text: str) -> list[dict[str, Any]]:
    subject = text.strip()

    if not subject:
        raise ValueError("Input cannot be empty")

    return [
        {
            "id": "H-001",
            "statement": (
                f"قد تكون هناك عوامل متعددة تؤثر في: {subject}"
            ),
            "status": "untested",
            "confidence": None,
            "evidence_needed": [
                "بيانات مباشرة مرتبطة بالموضوع",
                "مصدر مستقل للتحقق",
                "اختبار قابل للتكرار",
            ],
            "falsification": (
                "تُرفض الفرضية إذا أظهرت الأدلة "
                "عدم وجود علاقة بين العوامل المفترضة والموضوع."
            ),
        },
        {
            "id": "H-002",
            "statement": (
                "قد يؤدي نقص المعلومات إلى استنتاج غير دقيق."
            ),
            "status": "untested",
            "confidence": None,
            "evidence_needed": [
                "تحديد المعلومات الناقصة",
                "مقارنة مصادر متعددة",
            ],
            "falsification": (
                "تُراجع الفرضية إذا ثبت اكتمال المعلومات "
                "ودقتها بصورة مستقلة."
            ),
        },
  ]
