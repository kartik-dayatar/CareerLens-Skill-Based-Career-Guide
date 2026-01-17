from pydantic import BaseModel


class UserSkillCreate(BaseModel):
    user_id: int
    skill_id: int
    self_rating: int  # 1 to 10


class UserSkillResponse(BaseModel):
    id: int
    user_id: int
    skill_id: int
    self_rating: int

    class Config:
        orm_mode = True
