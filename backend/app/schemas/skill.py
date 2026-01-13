from pydantic import BaseModel


class SkillCreate(BaseModel):
    name: str
    skill_type: str  # technical / soft


class SkillResponse(BaseModel):
    id: int
    name: str
    skill_type: str

    class Config:
        orm_mode = True
