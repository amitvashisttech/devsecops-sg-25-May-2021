# Configure the AWS Provider
provider "aws" {
  region = "us-east-2"
  #access_key = "my-access-key"
  #secret_key = "my-secret-key"
}

resource "aws_instance" "web" {
  # Ubuntu 16.04
  #ami           = "ami-0d563aeddd4be7fff"
  # Amzone Linux
  ami           = "ami-077e31c4939f6a2f3"
  instance_type = "t2.micro"

  tags = {
    Name = "HelloWorld"
  }
}
