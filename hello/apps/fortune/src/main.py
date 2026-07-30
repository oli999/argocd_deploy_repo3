# fortune/src/main.py 파일

from fastapi import FastAPI

app = FastAPI()

@app.get("/fortune")
def get_fortune():
    return {
        "service": "fortune", 
        "message": "오후에 엄청 더워요"
    }