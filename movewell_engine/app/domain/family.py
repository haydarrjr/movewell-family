"""Domain entity models for Family Member profiles and posture baselines."""
from enum import Enum
from pydantic import BaseModel, Field


class MobilityLevel(str, Enum):
    REHABILITATION = "rehabilitation"
    LIGHT_ACTIVE = "light_active"
    MODERATE = "moderate"
    ATHLETIC = "athletic"


class RehabGoal(BaseModel):
    target_area: str = Field(..., description="Focus anatomical area, e.g., 'lower_back', 'shoulder_rotator', 'knee_patella'")
    primary_objective: str = Field(..., description="Goal description, e.g., 'Increase lumbar spine stability'")
    max_recommended_intensity: int = Field(default=5, ge=1, le=10)


class MovementReadiness(BaseModel):
    sleep_score: float = Field(..., ge=0.0, le=100.0)
    fatigue_level: int = Field(..., ge=1, le=10)
    pain_level: int = Field(..., ge=0, le=10)
    reported_symptoms: list[str] = Field(default_factory=list)

    @property
    def readiness_score(self) -> float:
        """Calculates a normalized 0-100 daily movement readiness score."""
        base = self.sleep_score * 0.5
        fatigue_penalty = (self.fatigue_level / 10.0) * 30.0
        pain_penalty = (self.pain_level / 10.0) * 40.0
        return max(0.0, min(100.0, base + 50.0 - fatigue_penalty - pain_penalty))


class FamilyMemberProfile(BaseModel):
    member_id: str
    display_name: str
    age_group: str = Field(..., description="e.g., 'child', 'adult', 'senior'")
    mobility_level: MobilityLevel = MobilityLevel.LIGHT_ACTIVE
    active_goals: list[RehabGoal] = Field(default_factory=list)
    restricted_joint_movements: list[str] = Field(default_factory=list)
