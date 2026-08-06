from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

app = FastAPI(
    title="DeployStack API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "DeployStack API",
        "version": "1.0.0",
    }


@app.get("/health/db")
def database_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "database": "connected"
    }
