output "ec2_instance_id" {
  value = aws_instance.finops_ec2.id
}

output "rds_endpoint" {
  value = aws_db_instance.finops_rds.endpoint
}

output "cur_bucket_name" {
  value = aws_s3_bucket.cur_bucket.bucket
}

output "athena_database_name" {
  value = aws_athena_database.finops_db.name
}