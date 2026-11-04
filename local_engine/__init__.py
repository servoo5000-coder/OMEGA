"""
OMEGA Local Intelligence Engine

Core modules:
- Planner
- Hypothesis Generator
- Critical Reviewer
"""

from .planner import build_plan
from .hypothesis import generate_hypotheses
from .critic import review_analysis

__all__ = [
    "build_plan",
    "generate_hypotheses",
    "review_analysis",
]
