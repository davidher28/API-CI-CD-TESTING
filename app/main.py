from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world() -> dict:
    return {"message": "Hello World"}
