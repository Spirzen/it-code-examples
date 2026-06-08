import { DataSource } from "typeorm";
import { User } from "./entity/User.js";

export const AppDataSource = new DataSource({
  type: "postgres",
  host: "localhost",
  port: 5432,
  username: "app",
  password: "secret",
  database: "app_db",
  entities: [User],
  synchronize: false, // только dev с осторожностью!
  migrations: ["dist/migrations/*.js"],
});

await AppDataSource.initialize();
