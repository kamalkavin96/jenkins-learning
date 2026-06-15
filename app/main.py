from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI"
    }

@app.get("/status")
def home():
    return {
        "message": "Running..."
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }