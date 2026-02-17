from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.tenant import Tenant
from app.models.user import User
from app.security.password import hash_password
from pydantic import BaseModel, EmailStr
from app.schemas.auth import RegisterRequest
from app.schemas.auth import LoginRequest
from app.security.password import verify_password
from app.security.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# class RegisterRequest(BaseModel):
#     email: EmailStr
#     password: str
#     tenant_name: str        

@router.post("/register")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    tenant = Tenant(name=payload.tenant_name)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    user = User(
        tenant_id=tenant.id,
        email=payload.email,
        password_hash=hash_password(payload.password)
    )

    db.add(user)
    db.commit()

    return {
        "message": "User created",
        "tenant_id": str(tenant.id)
    }

@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()

    if not user:
        return {"error": "Invalid credentials"}

    if not verify_password(payload.password, user.password_hash):
        return {"error": "Invalid credentials"}

    token = create_access_token({
        "sub": str(user.id),
        "tenant_id": str(user.tenant_id)
    })

    return {"access_token": token, "token_type": "bearer"}
