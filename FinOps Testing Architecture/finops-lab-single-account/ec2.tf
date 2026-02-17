resource "aws_instance" "finops_ec2" {
  ami           = "ami-0f58b397bc5c1f2e8"
  instance_type = var.instance_type

  tags = {
    Name        = "finops-ec2"
    Environment = var.environment
    Owner       = "FinOpsTeam"
  }
}