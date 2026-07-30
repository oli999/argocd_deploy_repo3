# fortune/src/main.py 파일

from fastapi import FastAPI

app = FastAPI()

@app.get("/fortune")
def get_fortune():
    return {
        "service": "fortune", 
        "message": "다음주에는 40도가 넘어가요 ㅜㅜ"
    }