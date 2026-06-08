using Microsoft.AspNetCore.Mvc;
using Minio;
using Minio.DataModel.Args;
using Minio.Exceptions;
using S3MediaManager.Models;
using System.IO;
using Microsoft.EntityFrameworkCore;

namespace S3MediaManager.Controllers
{
	[Route("api/[controller]")]
	[ApiController]
	public class FilesController : ControllerBase
	{
		private readonly IMinioClient _minioClient;
		private readonly ApplicationDbContext _context;
		private readonly IConfiguration _config;

		public FilesController(IMinioClient minioClient, ApplicationDbContext context, IConfiguration config)
		{
			_minioClient = minioClient;
			_context = context;
			_config = config;
		}

		[HttpPost("upload")]
		[RequestSizeLimit(500 * 1024 * 1024)]
		public async Task<IActionResult> UploadFile(IFormFile file)
		{
			if (file == null || file.Length == 0)
				return BadRequest("Файл не выбран или пуст.");

			try
			{
				var extension = Path.GetExtension(file.FileName);
				var uniqueFileName = $"{Guid.NewGuid()}{extension}";
				var bucketName = _config["S3:BucketName"];

				await using var stream = new MemoryStream();
				await file.CopyToAsync(stream);
				stream.Position = 0;

				// Проверка и создание бакета при необходимости
				try
				{
					await _minioClient.BucketExistsAsync(new BucketExistsArgs().WithBucket(bucketName));
				}
				catch (BucketNotFoundException)
				{
					await _minioClient.MakeBucketAsync(new MakeBucketArgs().WithBucket(bucketName));
				}

				// Загрузка файла
				await _minioClient.PutObjectAsync(new PutObjectArgs()
					.WithBucket(bucketName)
					.WithObject(uniqueFileName)
					.WithStreamData(stream)
					.WithObjectSize(file.Length)
					.WithContentType(file.ContentType ?? "application/octet-stream"));

				// Сохранение метаданных
				var metadata = new FileMetadata
				{
					OriginalName = file.FileName,
					S3Key = uniqueFileName,
					Size = file.Length,
					ContentType = file.ContentType ?? "application/octet-stream",
					CreatedAt = DateTime.UtcNow
				};

				_context.Files.Add(metadata);
				await _context.SaveChangesAsync();

				return Ok(new
				{
					message = "Файл успешно загружен",
					fileName = uniqueFileName,
					originalName = file.FileName,
					size = file.Length
				});
			}
			catch (Exception ex)
			{
				return StatusCode(500, $"Ошибка S3: {ex.Message}");
			}
		}

		[HttpGet]
		public async Task<ActionResult<IEnumerable<FileMetadata>>> GetFiles()
		{
			return await _context.Files.ToListAsync();
		}

		[HttpDelete("{id}")]
		public async Task<IActionResult> DeleteFile(int id)
		{
			var file = await _context.Files.FindAsync(id);
			if (file == null)
				return NotFound();

			try
			{
				var bucketName = _config["S3:BucketName"];
				await _minioClient.RemoveObjectAsync(new RemoveObjectArgs()
					.WithBucket(bucketName)
					.WithObject(file.S3Key));

				_context.Files.Remove(file);
				await _context.SaveChangesAsync();

				return NoContent();
			}
			catch (Exception ex)
			{
				return StatusCode(500, "Ошибка удаления файла");
			}
		}
	}
}
