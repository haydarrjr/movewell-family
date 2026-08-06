"""Unit tests for Movewell Engine clinical safety & coaching orchestrator."""
import pytest
from app.domain.family import FamilyMemberProfile, MovementReadiness, MobilityLevel
from app.services.safety_hardguard import SafetyHardguardEngine
from app.services.coaching_orchestrator import CoachingOrchestrator


def test_movement_readiness_score():
    readiness = MovementReadiness(
        sleep_score=80.0,
        fatigue_level=3,
        pain_level=1
    )
    score = readiness.readiness_score
    assert 70.0 <= score <= 100.0


def test_safety_hardguard_acute_pain_blocks_exercise():
    profile = FamilyMemberProfile(
        member_id="fam_01",
        display_name="Jane Doe",
        age_group="adult",
        mobility_level=MobilityLevel.LIGHT_ACTIVE
    )
    # High pain level (8/10)
    readiness = MovementReadiness(
        sleep_score=50.0,
        fatigue_level=6,
        pain_level=8
    )

    result = SafetyHardguardEngine.validate_routine(
        profile=profile,
        readiness=readiness,
        proposed_exercise_tags=["squats", "lower_body"],
        proposed_intensity=6
    )

    assert result.is_safe is False
    assert result.status == "blocked"
    assert len(result.blocked_reasons) > 0


def test_coaching_orchestrator_recommendation():
    profile = FamilyMemberProfile(
        member_id="fam_02",
        display_name="John Doe",
        age_group="adult",
        mobility_level=MobilityLevel.MODERATE
    )
    readiness = MovementReadiness(
        sleep_score=85.0,
        fatigue_level=2,
        pain_level=0
    )

    orchestrator = CoachingOrchestrator()
    rec = orchestrator.generate_daily_routine(profile, readiness)

    assert rec.member_id == "fam_02"
    assert rec.readiness_score > 75.0
    assert rec.safety_result.is_safe is True
    assert len(rec.exercises) > 0
