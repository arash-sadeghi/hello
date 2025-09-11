from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # return "salamun alaykum sohrab"
    return {
        "message": "salamun alaykum sohrab",
        "status": "success",
        "location": "tehran"
        }