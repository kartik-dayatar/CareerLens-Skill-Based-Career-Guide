from fastapi import FastAPI
from app.database import engine
from app.models import User, Skill, UserSkill

app = FastAPI()

User.metadata.create_all(bind=engine)
Skill.metadata.create_all(bind=engine)
UserSkill.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "CareerLens backend with user and skill tables running"}
