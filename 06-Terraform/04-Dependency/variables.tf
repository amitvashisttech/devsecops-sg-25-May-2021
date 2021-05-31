provider "aws" {
  region  = "us-east-2"
  version = ">=3.7,<=3.11"
}


resource "aws_instance" "frontend" {
  ami           = "ami-077e31c4939f6a2f3"
  instance_type = "t2.micro"
  count         = 1
  depends_on    = [aws_instance.backend]
  tags = {
    Name = "Frontend"
  }
}




resource "aws_instance" "backend" {
  ami           = "ami-077e31c4939f6a2f3"
  instance_type = "t2.micro"
  tags = {
    Name = "Backend"
  }
}
