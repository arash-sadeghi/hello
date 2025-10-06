from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "salamun alaykum iren",
        "status": "success",
        "location": "tehran"
        }