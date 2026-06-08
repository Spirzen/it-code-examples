using Microsoft.EntityFrameworkCore;
using Npgsql;
using S3MediaManager.Models;
using Swashbuckle.AspNetCore;
using Minio;
using Minio.DataModel.Args;

var builder = WebApplication.CreateBuilder(args);

// 1. Регистрация базы данных (PostgreSQL)
builder.Services.AddDbContext<ApplicationDbContext>(options =>
	options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));

// 2. Регистрация настроек S3
builder.Services.Configure<S3Settings>(builder.Configuration.GetSection("S3"));

// 3. Регистрация клиента MinIO
builder.Services.AddSingleton<IMinioClient>(sp =>
{
	var config = sp.GetRequiredService<IConfiguration>();
	var endpoint = config["S3:Endpoint"]?.Replace("http://", "").Replace("https://", "") ?? "localhost:9000";
	var accessKey = config["S3:AccessKey"] ?? "minioadmin";
	var secretKey = config["S3:SecretKey"] ?? "minioadmin";

	return new MinioClient()
		.WithEndpoint(endpoint)
		.WithCredentials(accessKey, secretKey)
		.Build();
});

// 4. Регистрация контроллеров
builder.Services.AddControllers();

// 5. Настройка Swagger
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
	app.UseSwagger();
	app.UseSwaggerUI();
}

app.UseAuthorization();
app.MapControllers();

app.Run();

namespace S3MediaManager.Models
{
	public class S3Settings
	{
		public string Endpoint { get; set; } = "";
		public string Region { get; set; } = "";
		public string BucketName { get; set; } = "";
		public bool UseSSL { get; set; }
		public string AccessKey { get; set; } = "";
		public string SecretKey { get; set; } = "";
	}

	public class ApplicationDbContext : DbContext
	{
		public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

		public DbSet<FileMetadata> Files { get; set; }
	}

	public class FileMetadata
	{
		public int Id { get; set; }
		public string OriginalName { get; set; } = "";
		public string S3Key { get; set; } = "";
		public long Size { get; set; }
		public string ContentType { get; set; } = "";
		public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
	}
}
