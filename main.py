from fastapi import FastAPI
from typing import List


app = FastAPI()

@app.get("/")
async def root() -> None:
    return {"message": "Hello World"}
