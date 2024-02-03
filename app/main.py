from fastapi import FastAPI

app = FastAPI()


def hello_world() -> str:
    return "Hello World!"


@app.get("/")
async def read_main() -> dict[str, str]:
    return {"message": hello_world()}
