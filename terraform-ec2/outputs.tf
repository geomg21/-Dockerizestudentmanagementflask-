output "ec2_public_ip" {
  value = aws_instance.app_ec2.public_ip
}

output "ec2_public_dns" {
  value = aws_instance.app_ec2.public_dns
}

output "vpc_id" {
  value = aws_vpc.app_vpc.id
}

output "security_group_id" {
  value = aws_security_group.app_sg.id
}
