from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillBulkCreate, SkillResponse

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


# -------- Get all skills --------
@router.get("/", response_model=list[SkillResponse])
def get_all_skills(db: Session = Depends(get_db)):
    return db.query(Skill).all()


# -------- Create single skill --------
@router.post("/", response_model=SkillResponse)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    existing = db.query(Skill).filter(Skill.name == skill.name).first()
    if existing:
        return existing

    new_skill = Skill(
        name=skill.name,
        skill_type=skill.skill_type
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


# -------- Bulk create skills --------
@router.post("/bulk", response_model=list[SkillResponse])
def create_skills_bulk(
    payload: SkillBulkCreate,
    db: Session = Depends(get_db)
):
    result = []

    for skill_data in payload.skills:
        existing = (
            db.query(Skill)
            .filter(Skill.name == skill_data.name)
            .first()
        )

        if existing:
            result.append(existing)
            continue

        skill = Skill(
            name=skill_data.name,
            skill_type=skill_data.skill_type
        )
        db.add(skill)
        db.flush()
        result.append(skill)

    db.commit()
    return result
