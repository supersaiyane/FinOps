resource "aws_s3_bucket" "cur_bucket" {
  bucket = "finops-cur-bucket-${random_id.suffix.hex}"
}

resource "aws_s3_bucket" "athena_results" {
  bucket = "finops-athena-results-${random_id.suffix.hex}"
}