"""Movewell Family Engine - Main FastAPI Application."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.domain.family import FamilyMemberProfile, MovementReadiness
from app.services.coaching_orchestrator import CoachingOrchestrator, RoutineRecommendation

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Open-source AI-powered family movement health & physical rehabilitation platform."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = CoachingOrchestrator()


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "environment": settings.environment,
        "version": "1.0.0"
    }


@app.post("/api/v1/recommendation", response_model=RoutineRecommendation)
def generate_recommendation(payload: dict):
    try:
        profile_data = payload.get("profile")
        readiness_data = payload.get("readiness")

        if not profile_data or not readiness_data:
            raise HTTPException(status_code=400, detail="Missing 'profile' or 'readiness' payload.")

        profile = FamilyMemberProfile(**profile_data)
        readiness = MovementReadiness(**readiness_data)

        return orchestrator.generate_daily_routine(profile, readiness)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
