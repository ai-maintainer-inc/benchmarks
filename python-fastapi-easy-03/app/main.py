from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def read_hello():
    return {"message": "pong"}
