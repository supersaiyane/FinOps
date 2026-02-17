from fastapi import FastAPI, Depends
from app.db.session import engine
from app.models.base import Base

# Import models so SQLAlchemy registers them
from app.models import cloud_account

# Import routers
from app.api.auth import router as auth_router
from app.api.cloud import router as cloud_router

from app.security.dependencies import get_current_user

# Create app FIRST
app = FastAPI(title="Samaira Cloud Intelligence")

# Create tables on startup
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

# Include routers AFTER app creation
app.include_router(auth_router)
app.include_router(cloud_router)

@app.get("/")
def health_check():
    return {"status": "Samaira is running"}

@app.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "message": "Protected route working",
        "user": user
    }
