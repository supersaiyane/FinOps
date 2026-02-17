resource "aws_db_instance" "finops_rds" {
  allocated_storage    = 20
  engine               = "mysql"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = "Finops123!"
  skip_final_snapshot  = true

  tags = {
    Name        = "finops-rds"
    Environment = var.environment
  }
}