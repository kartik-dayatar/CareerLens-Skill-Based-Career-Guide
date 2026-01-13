from fastapi import FastAPI
from app.database import engine
from app.models import User, Skill, UserSkill
from app.api.user import router as user_router
from app.api.skill import router as skill_router

app = FastAPI()

User.metadata.create_all(bind=engine)
Skill.metadata.create_all(bind=engine)
UserSkill.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(skill_router)

@app.get("/")
def root():
    return {"message": "CareerLens backend running"}
