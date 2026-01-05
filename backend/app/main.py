from fastapi import FastAPI
from app.database import engine
from app.models import user

app = FastAPI()

# Create tables
user.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "CareerLens backend with DB running"}
