from pydantic import BaseModel
from typing import List


# -------- Base schema --------
class SkillBase(BaseModel):
    name: str
    skill_type: str


# -------- For input (single skill) --------
class SkillCreate(SkillBase):
    pass


# -------- For input (bulk skills) --------
class SkillBulkCreate(BaseModel):
    skills: List[SkillCreate]


# -------- For output (responses) --------
class SkillResponse(SkillBase):
    id: int

    class Config:
        orm_mode = True
