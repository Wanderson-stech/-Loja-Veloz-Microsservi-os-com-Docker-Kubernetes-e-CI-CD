provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "loja_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = { Name = "loja-veloz-vpc" }
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "loja-veloz-cluster"
  cluster_version = "1.27"
  subnet_ids      = ["subnet-example-1", "subnet-example-2"]
  vpc_id          = aws_vpc.loja_vpc.id

  eks_managed_node_groups = {
    general = {
      desired_size = 2
      instance_types = ["t3.medium"]
    }
  }
}

resource "aws_db_instance" "default" {
  allocated_storage    = 10
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  db_name              = "lojaveloz"
  username             = var.db_user
  password             = var.db_password
  skip_final_snapshot  = true
}