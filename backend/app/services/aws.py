import boto3
from botocore.exceptions import ClientError
from app.security.encryption import decrypt

def test_assume_role(role_arn: str, external_id: str):
    try:
        sts = boto3.client("sts")
        response = sts.assume_role(
            RoleArn=role_arn,
            RoleSessionName="samaira-session",
            ExternalId=external_id
        )
        return response["Credentials"]
    except ClientError as e:
        raise Exception(f"AssumeRole failed: {str(e)}")
