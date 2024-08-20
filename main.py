from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/")
async def root():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos")
        data = response.json()

    return data
