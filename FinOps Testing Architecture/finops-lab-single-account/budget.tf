resource "aws_budgets_budget" "monthly_budget" {
  name        = "finops-monthly-budget"
  budget_type = "COST"
  limit_amount = "50"
  limit_unit   = "USD"
  time_unit    = "MONTHLY"

  notification {
    comparison_operator = "GREATER_THAN"
    threshold           = 80
    threshold_type      = "PERCENTAGE"
    notification_type   = "FORECASTED"

    subscriber_email_addresses = ["your-email@example.com"]
  }
}