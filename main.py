from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "hello bernard",
        "status": "success",
        "location": "st. john's"
        }