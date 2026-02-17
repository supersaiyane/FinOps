from pydantic import BaseModel

class AWSAccountCreate(BaseModel):
    account_name: str
    account_id: str
    role_arn: str
