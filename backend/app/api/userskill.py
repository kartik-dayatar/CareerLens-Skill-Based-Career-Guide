from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.userskill import UserSkill
from app.models.user import User
from app.models.skill import Skill
from app.schemas.userskill import UserSkillCreate, UserSkillResponse

router = APIRouter(prefix="/user-skills", tags=["User Skills"])


# 1️⃣ Assign Skill to User
@router.post("/", response_model=UserSkillResponse)
def assign_skill_to_user(data: UserSkillCreate, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if skill exists
    skill = db.query(Skill).filter(Skill.id == data.skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    # Prevent duplicate assignment
    existing = db.query(UserSkill).filter(
        UserSkill.user_id == data.user_id,
        UserSkill.skill_id == data.skill_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Skill already assigned to user")

    user_skill = UserSkill(
        user_id=data.user_id,
        skill_id=data.skill_id,
        self_rating=data.self_rating
    )

    db.add(user_skill)
    db.commit()
    db.refresh(user_skill)
    return user_skill


# 2️⃣ Get all skills of a user
@router.get("/user/{user_id}", response_model=list[UserSkillResponse])
def get_skills_of_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(UserSkill).filter(UserSkill.user_id == user_id).all()
