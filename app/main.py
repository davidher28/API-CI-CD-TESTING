from fastapi import FastAPI

from app.services.hello_world import hello_world

app = FastAPI()


@app.get("/")
async def read_main() -> dict:
    message: str = hello_world()
    return {"message": message}
