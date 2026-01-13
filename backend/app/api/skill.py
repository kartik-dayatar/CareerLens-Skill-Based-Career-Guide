from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillResponse

router = APIRouter(prefix="/skills", tags=["Skills"])


# 1️⃣ Create Skill
@router.post("/", response_model=SkillResponse)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    existing_skill = db.query(Skill).filter(Skill.name == skill.name).first()
    if existing_skill:
        raise HTTPException(status_code=400, detail="Skill already exists")

    new_skill = Skill(
        name=skill.name,
        skill_type=skill.skill_type
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


# 2️⃣ Get All Skills
@router.get("/", response_model=list[SkillResponse])
def get_all_skills(db: Session = Depends(get_db)):
    return db.query(Skill).all()


# 3️⃣ Get Skill by ID
@router.get("/{skill_id}", response_model=SkillResponse)
def get_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill
