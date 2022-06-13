from fastapi import FastAPI

app = FastAPI()


@app.get("/navbar")
async def root():
    return {"message": "Hello World"}
