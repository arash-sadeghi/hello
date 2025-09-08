from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "hi Daniel FIADJOE how are you doing in this cloudy day"