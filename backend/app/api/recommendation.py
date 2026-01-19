from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.userskill import UserSkill
from app.models.skill import Skill
from app.core.role_recommender import recommend_roles

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


@router.get("/user/{user_id}")
def get_role_recommendations(user_id: int, db: Session = Depends(get_db)):
    user_skills = (
        db.query(Skill.name, UserSkill.self_rating)
        .join(UserSkill, Skill.id == UserSkill.skill_id)
        .filter(UserSkill.user_id == user_id)
        .all()
    )

    if not user_skills:
        raise HTTPException(status_code=404, detail="No skills found for user")

    skill_dict = {name: rating for name, rating in user_skills}

    recommendations = recommend_roles(skill_dict)

    return {
        "user_id": user_id,
        "recommendations": recommendations
    }
