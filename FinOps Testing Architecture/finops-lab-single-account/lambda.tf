resource "aws_iam_role" "lambda_role" {
  name = "finops_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "anomaly_detector" {
  function_name = "finops-anomaly-detector"
  handler       = "anomaly.lambda_handler"
  runtime       = "python3.9"
  role          = aws_iam_role.lambda_role.arn
  filename      = "lambda.zip"

  environment {
    variables = {
      ATHENA_DB     = aws_athena_database.finops_db.name
      ATHENA_TABLE  = "finops_cur"
      SNS_TOPIC     = aws_sns_topic.finops_alerts.arn
      ATHENA_OUTPUT = "s3://${aws_s3_bucket.athena_results.bucket}/"
    }
  }
}
