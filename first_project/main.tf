provider "aws" {
    region = "ap-south-1"
  
}
resource "aws_instance" "first_server" {
    ami = "ami-0614680123427b75e"
    instance_type = "t2.micro"
    key_name = "first-key"

tags = {
  Name = "first_server"
}
  
}