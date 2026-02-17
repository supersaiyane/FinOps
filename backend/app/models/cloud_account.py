import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.models.base import Base

class CloudAccount(Base):
    __tablename__ = "cloud_accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)

    cloud_provider = Column(String, nullable=False)  # AWS for now
    account_name = Column(String, nullable=False)
    account_id = Column(String, nullable=False)

    role_arn_encrypted = Column(String, nullable=False)
    external_id_encrypted = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
