[Table("Users")]
public class User
{
    [Key]                          // Указывает, что это первичный ключ
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]  // Автоинкремент
    public int Id { get; set; }

    [Required]                     // NOT NULL в БД
    [MaxLength(100)]               // Ограничение длины (NVARCHAR(100))
    public string Name { get; set; }

    [MaxLength(200)]               // NULL в БД (по умолчанию, если не Required)
    public string? Address { get; set; }  // "?" означает, что может быть null

    [Required]
    [MaxLength(100)]
    [EmailAddress]                 // Проверка формата email
    public string Email { get; set; }
}

