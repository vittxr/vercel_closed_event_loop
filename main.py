from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    # Simulate an async operation with a 2-second delay
    await asyncio.sleep(2)
    return {"message": "Hello World"}
