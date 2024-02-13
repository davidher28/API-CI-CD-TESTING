from fastapi import FastAPI

app = FastAPI()


def hello_world() -> str:
    return "Hello Barcelona!"


@app.get("/")
async def read_main() -> dict:
    message: str = hello_world()
    return {"message": message}
