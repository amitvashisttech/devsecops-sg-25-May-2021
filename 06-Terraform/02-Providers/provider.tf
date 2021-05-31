provider "aws" {
  region = "us-east-2"
  version = ">=3.7,<=3.11"
}


provider "aws" {
  region = "us-west-2"
  version = ">=3.7,<=3.11"
  alias  = "us-west-2"
}


resource "aws_instance" "example_east" {
  ami           = "ami-077e31c4939f6a2f3"
  instance_type = "t2.micro"

  tags = {
    Name = "HelloWorld-East-1"
  }
}



resource "aws_instance" "example_west" {
  ami           = "ami-0cf6f5c8a62fa5da6"
  instance_type = "t2.micro"
  provider   = aws.us-west-2

  tags = {
    Name = "HelloWorld-West-1"
  }
}
