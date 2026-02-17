resource "aws_sns_topic" "finops_alerts" {
  name = "finops-cost-alerts"
}

resource "aws_sns_topic_subscription" "email_alert" {
  topic_arn = aws_sns_topic.finops_alerts.arn
  protocol  = "email"
  endpoint  = "your-email@example.com"
}
