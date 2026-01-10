# app/core/agent/models.py
from dataclasses import dataclass
from typing import List
from app.core.scoring.readiness import Persona

@dataclass
class PersonaSelectionResult:
    persona: Persona
    reasons: List[str]

@dataclass
class ContributionReadinessResult:
    persona: Persona
    readiness_score: int
    reasons: List[str]
