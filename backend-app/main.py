from fastapi import FastAPI

app = FastAPI()

@app.get("/api/greet")
def greet():
    return {"message": "Hello from the FastAPI backend!"}