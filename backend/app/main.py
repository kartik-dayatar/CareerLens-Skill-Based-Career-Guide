from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CareerLens backend running perfectly and setup is complete"}

