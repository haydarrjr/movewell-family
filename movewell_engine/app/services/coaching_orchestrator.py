"""Coaching Orchestrator Service.

Generates personalized, safety-verified family movement protocols.
"""
from pydantic import BaseModel
from app.domain.family import FamilyMemberProfile, MovementReadiness
from app.services.safety_hardguard import SafetyHardguardEngine, SafetyValidationResult


class RoutineRecommendation(BaseModel):
    member_id: str
    readiness_score: float
    routine_name: str
    exercises: list[dict]
    safety_result: SafetyValidationResult


class CoachingOrchestrator:
    """Orchestrates adaptive posture and movement recommendations."""

    def __init__(self, safety_engine: SafetyHardguardEngine | None = None):
        self.safety_engine = safety_engine or SafetyHardguardEngine()

    def generate_daily_routine(
        self,
        profile: FamilyMemberProfile,
        readiness: MovementReadiness
    ) -> RoutineRecommendation:
        score = readiness.readiness_score

        # Select exercise pool based on readiness
        if score >= 75:
            routine_name = "Optimal Movement & Mobility Flow"
            proposed_exercises = [
                {"name": "Thoracic Spine Extension", "tag": "spine_mobility", "intensity": 4},
                {"name": "Bodyweight Squat to Posture Hold", "tag": "lower_body", "intensity": 5},
                {"name": "Wall Slide Arm Raises", "tag": "shoulder_scapular", "intensity": 3}
            ]
            proposed_intensity = 5
        elif score >= 45:
            routine_name = "Gentle Postural Reset"
            proposed_exercises = [
                {"name": "Seated Cat-Cow Stretch", "tag": "spine_gentle", "intensity": 2},
                {"name": "Chin Tucks & Neck Retraction", "tag": "cervical_posture", "intensity": 2},
                {"name": "Diaphragmatic Breathing", "tag": "recovery", "intensity": 1}
            ]
            proposed_intensity = 2
        else:
            routine_name = "Restorative Decompression Protocol"
            proposed_exercises = [
                {"name": "Supine Lumbar Decompression", "tag": "passive_rest", "intensity": 1},
                {"name": "Guided Deep Breathing", "tag": "recovery", "intensity": 1}
            ]
            proposed_intensity = 1

        tags = [e["tag"] for e in proposed_exercises]
        safety_check = self.safety_engine.validate_routine(
            profile=profile,
            readiness=readiness,
            proposed_exercise_tags=tags,
            proposed_intensity=proposed_intensity
        )

        return RoutineRecommendation(
            member_id=profile.member_id,
            readiness_score=score,
            routine_name=routine_name if safety_check.is_safe else f"[MODIFIED] {routine_name}",
            exercises=proposed_exercises if safety_check.is_safe else [
                {"name": "Gentle Breathing & Passive Rest", "tag": "passive_rest", "intensity": 1}
            ],
            safety_result=safety_check
        )
