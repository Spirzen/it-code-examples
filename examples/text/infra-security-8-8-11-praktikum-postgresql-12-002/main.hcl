resource "aws_db_instance" "app" {
  identifier             = "app-postgres"
  engine                 = "postgres"
  engine_version         = "16.3"
  instance_class         = "db.r6g.large"
  allocated_storage      = 100
  max_allocated_storage  = 500
  storage_encrypted      = true

  db_name  = "appdb"
  username = "app"
  password = var.db_password

  multi_az               = true
  backup_retention_period = 14
  backup_window          = "03:00-04:00"

  parameter_group_name = aws_db_parameter_group.app.name
  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.db.name

  deletion_protection = true
  skip_final_snapshot = false
  final_snapshot_identifier = "app-postgres-final"
}

resource "aws_db_parameter_group" "app" {
  family = "postgres16"
  parameter {
    name  = "log_min_duration_statement"
    value = "500"
  }
  parameter {
    name  = "shared_preload_libraries"
    value = "pg_stat_statements"
  }
}
