from typing import Any


def build_plan(
    text: str,
    max_steps: int = 5,
    mode: str = "general",
) -> dict[str, Any]:

    subject = text.strip()

    if not subject:
        raise ValueError("Analysis input cannot be empty")

    workflows = {
        "general": [
            "تحديد السؤال والهدف",
            "تفكيك الموضوع إلى عناصر",
            "جمع المعلومات المتاحة",
            "تحديد الفرضيات المحتملة",
            "اختبار الفرضيات",
            "مراجعة النتائج والقيود",
            "استخلاص النتائج",
        ],
        "technical": [
            "تحديد النظام والمشكلة",
            "تحديد المكونات والاعتماديات",
            "تحليل المدخلات والمخرجات",
            "تحديد أسباب الخلل المحتملة",
            "تصميم اختبارات آمنة",
            "مراجعة النتائج",
            "اقتراح التحسينات",
        ],
        "scientific": [
            "صياغة السؤال العلمي",
            "تحديد المتغيرات",
            "مراجعة المعرفة المتاحة",
            "صياغة فرضيات قابلة للاختبار",
            "تصميم تجربة قابلة للتكرار",
            "تحليل الأدلة",
            "تحديد حدود الاستنتاج",
        ],
    }

    steps = workflows.get(mode, workflows["general"])

    return {
        "objective": subject,
        "method": mode,
        "steps": [
            {
                "number": index + 1,
                "action": step,
            }
            for index, step in enumerate(steps[:max_steps])
        ],
        "step_count": min(max_steps, len(steps)),
        "status": "planned",
  }
