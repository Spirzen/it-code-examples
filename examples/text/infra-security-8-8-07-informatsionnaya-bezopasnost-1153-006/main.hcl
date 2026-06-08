# modules/vpc/variables.tf
variable "environment" {
  description = "Имя окружения"
  type        = string
}

variable "cidr_block" {
  description = "CIDR-блок VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnets" {
  description = "CIDR-блоки публичных подсетей"
  type        = list(string)
}

variable "private_subnets" {
  description = "CIDR-блоки приватных подсетей"
  type        = list(string)
}

variable "tags" {
  description = "Общие теги ресурсов"
  type        = map(string)
  default     = {}
}
