from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "I love fofo food",
        "status": "success",
        "location": "st. john's"
        }