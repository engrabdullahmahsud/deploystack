from fastapi import FastAPI

app = FastAPI(
    title="DeployStack API",
    version="0.1.0",
    description="Self-hosted deployment platform API"
)

@app.get("/")
def root():
    return {"message": "Welcome to DeployStack"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "DeployStack API"
    }
