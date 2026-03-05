from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.models import User, Skill, UserSkill
from app.api.user import router as user_router
from app.api.skill import router as skill_router
from app.api.userskill import router as userskill_router
from app.api.recommendation import router as recommendation_router

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(skill_router)
app.include_router(userskill_router)
app.include_router(recommendation_router)




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
