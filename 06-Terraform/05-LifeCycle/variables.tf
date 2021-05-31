provider "aws" {
  region  = "us-east-2"
  version = ">=3.7,<=3.11"
}


resource "aws_instance" "frontend" {
  ami           = "ami-077e31c4939f6a2f3"
  # ami		= "ami-0ebc8f6f580a04647"
  instance_type = "t2.micro"
  depends_on    = [aws_instance.backend]
  lifecycle { 
    create_before_destroy = true
  }
  tags = {
    Name = "Frontend"
  }
}




resource "aws_instance" "backend" {
  ami           = "ami-077e31c4939f6a2f3"
  instance_type = "t2.micro"
  count         = 1
  lifecycle { 
    prevent_destroy = false
  }
  tags = {
    Name = "Backend"
  }
}
