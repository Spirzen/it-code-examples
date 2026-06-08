const crypto = require('crypto');

const text = "Привет, мир!";
console.log(`Исходный текст: ${text}`);

// Хеширование SHA-256
const sha256Hash = crypto.createHash('sha256').update(text, 'utf8').digest('hex');
console.log(`SHA-256: ${sha256Hash}`);

// Хеширование MD5
const md5Hash = crypto.createHash('md5').update(text, 'utf8').digest('hex');
console.log(`MD5: ${md5Hash}`);

// Хеширование с солью для паролей
const password = "mySecretPassword123";
const salt = crypto.randomBytes(16).toString('hex');
const saltedPassword = password + salt;
const passwordHash = crypto.createHash('sha512').update(saltedPassword).digest('hex');

console.log(`Соль: ${salt}`);
console.log(`Хеш пароля: ${passwordHash}`);
