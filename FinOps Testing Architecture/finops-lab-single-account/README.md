# FinOps Single Account Terraform Lab

## Deploy

terraform init
terraform plan
terraform apply

## Destroy

terraform destroy

## What This Lab Creates

- EC2 instance
- RDS instance
- CUR enabled
- S3 bucket for billing
- Athena database + Glue table
- Budget alert

Wait 24 hours for CUR to populate before querying Athena.