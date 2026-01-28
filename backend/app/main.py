from fastapi import FastAPI
from app.database import engine
from app.models import User, Skill, UserSkill
from app.api.user import router as user_router
from app.api.skill import router as skill_router
from app.api.userskill import router as userskill_router
from app.api.recommendation import router as recommendation_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

User.metadata.create_all(bind=engine)
Skill.metadata.create_all(bind=engine)
UserSkill.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(skill_router)
app.include_router(userskill_router)
app.include_router(recommendation_router)


from fastapi import FastAPI




app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "CareerLens backend running"}
