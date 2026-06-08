# modules/vpc/outputs.tf
output "vpc_id" {
  description = "Идентификатор VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "Идентификаторы публичных подсетей"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Идентификаторы приватных подсетей"
  value       = aws_subnet.private[*].id
}
