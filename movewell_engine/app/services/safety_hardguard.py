"""Deterministic Clinical Safety Hardguard Engine.

Ensures that AI movement recommendations never bypass physical restrictions,
high pain levels, or acute fatigue flags.
"""
from pydantic import BaseModel
from app.domain.family import FamilyMemberProfile, MovementReadiness


class SafetyValidationResult(BaseModel):
    is_safe: bool
    status: str  # 'passed', 'blocked', 'modified_required'
    blocked_reasons: list[str] = []
    allowed_intensity_cap: int = 10


class SafetyHardguardEngine:
    """Non-bypassable clinical safety checker."""

    @staticmethod
    def validate_routine(
        profile: FamilyMemberProfile,
        readiness: MovementReadiness,
        proposed_exercise_tags: list[str],
        proposed_intensity: int
    ) -> SafetyValidationResult:
        reasons = []

        # 1. Acute Pain Hard Block (> 6/10 pain blocks all non-passive movement)
        if readiness.pain_level >= 7:
            reasons.append(f"Acute pain level ({readiness.pain_level}/10) exceeds clinical safety limit. Exercise blocked.")
            return SafetyValidationResult(
                is_safe=False,
                status="blocked",
                blocked_reasons=reasons,
                allowed_intensity_cap=1
            )

        # 2. High Fatigue Cap
        max_intensity = 10
        if readiness.fatigue_level >= 8:
            max_intensity = min(max_intensity, 3)
            reasons.append("Severe fatigue detected: intensity capped at 3/10.")

        # 3. Restricted Joint Movements Match
        for restriction in profile.restricted_joint_movements:
            for tag in proposed_exercise_tags:
                if restriction.lower() in tag.lower():
                    reasons.append(f"Proposed movement tag '{tag}' conflicts with restricted joint movement '{restriction}'.")

        # 4. Check intensity against proposed
        if proposed_intensity > max_intensity:
            reasons.append(f"Proposed intensity {proposed_intensity} exceeds allowed cap {max_intensity}.")

        if reasons:
            is_pass = False
            status = "blocked" if any("blocked" in r.lower() or "conflicts" in r.lower() for r in reasons) else "modified_required"
            return SafetyValidationResult(
                is_safe=is_pass,
                status=status,
                blocked_reasons=reasons,
                allowed_intensity_cap=max_intensity
            )

        return SafetyValidationResult(
            is_safe=True,
            status="passed",
            blocked_reasons=[],
            allowed_intensity_cap=max_intensity
        )
