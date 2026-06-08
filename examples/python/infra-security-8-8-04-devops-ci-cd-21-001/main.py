
import pulumi
import pulumi_aws as aws

# Создание VPC
vpc = aws.ec2.Vpc("my-vpc",
    cidr_block="10.0.0.0/16")

# Создание подсети
subnet = aws.ec2.Subnet("my-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24")

# Создание EC2-инстанса
instance = aws.ec2.Instance("web-server",
    instance_type="t3.micro",
    ami="ami-0abcdef1234567890",
    subnet_id=subnet.id)
