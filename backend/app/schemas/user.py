from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    education: str | None = None
    experience: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    education: str | None = None
    experience: str | None = None

    class Config:
        orm_mode = True
