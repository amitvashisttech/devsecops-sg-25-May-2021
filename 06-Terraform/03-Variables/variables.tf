provider "aws" {
  region  = "us-east-2"
  version = ">=3.7,<=3.11"
}

variable "zones" {
  default = ["us-east-2a", "us-east-2b"]
}


resource "aws_instance" "example_east" {
  ami               = "ami-077e31c4939f6a2f3"
  instance_type     = "t2.micro"
  count             = 2
  availability_zone = var.zones[count.index]
  tags = {
    Name = "HelloWorld"
  }
}
