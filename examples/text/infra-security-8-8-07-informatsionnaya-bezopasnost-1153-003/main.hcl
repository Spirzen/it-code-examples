# Terraform — декларативное описание AWS EC2 инстанса
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"
  
  tags = {
    Name        = "web-server"
    Environment = "production"
    ManagedBy   = "terraform"
  }
  
  root_block_device {
    volume_size = 50
    volume_type = "gp3"
    encrypted   = true
  }
  
  vpc_security_group_ids = [aws_security_group.web.id]
  subnet_id              = aws_subnet.private.id
  
  user_data = templatefile("${path.module}/startup.sh.tpl", {
    app_version = var.app_version
  })
}
