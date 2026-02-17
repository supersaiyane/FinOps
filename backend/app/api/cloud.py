import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.security.dependencies import get_current_user
from app.models.cloud_account import CloudAccount
from app.schemas.cloud import AWSAccountCreate
from app.security.encryption import encrypt
from app.services.aws import test_assume_role

router = APIRouter(prefix="/cloud", tags=["cloud"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/aws")
def add_aws_account(
    payload: AWSAccountCreate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    external_id = str(uuid.uuid4())

    # Test AssumeRole
    try:
        test_assume_role(payload.role_arn, external_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    cloud_account = CloudAccount(
        tenant_id=user["tenant_id"],
        cloud_provider="AWS",
        account_name=payload.account_name,
        account_id=payload.account_id,
        role_arn_encrypted=encrypt(payload.role_arn),
        external_id_encrypted=encrypt(external_id)
    )

    db.add(cloud_account)
    db.commit()

    return {"message": "AWS account added successfully"}
