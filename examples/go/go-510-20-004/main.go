  ctx := context.Background()
  req := testcontainers.ContainerRequest{
      Image:        "postgres:15",
      ExposedPorts: []string{"5432/tcp"},
      Env: map[string]string{
          "POSTGRES_DB":       "test",
          "POSTGRES_USER":     "test",
          "POSTGRES_PASSWORD": "test",
      },
  }
  pgContainer, err := testcontainers.GenericContainer(ctx, testcontainers.GenericContainerRequest{
      ContainerRequest: req,
      Started:          true,
  })
