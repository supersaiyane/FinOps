resource "aws_cur_report_definition" "cur" {
  report_name                = "finops-cur"
  time_unit                  = "DAILY"
  format                     = "Parquet"
  compression                = "Parquet"
  additional_schema_elements = ["RESOURCES"]
  s3_bucket                  = aws_s3_bucket.cur_bucket.bucket
  s3_prefix                  = "cur"
  s3_region                  = var.region
  additional_artifacts       = ["ATHENA"]
}