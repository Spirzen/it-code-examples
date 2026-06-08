use company_db;
const bucket = new GridFSBucket(db, { bucketName: "attachments" });

// Загрузка из строки (учебный пример; в приложении — поток из файла)
const buf = Buffer.from("PDF or image bytes here");
const uploadStream = bucket.openUploadStream("report.pdf", {
  metadata: { uploadedBy: "ivanov", contentType: "application/pdf" }
});
uploadStream.end(buf);

// Список файлов в bucket
db.getCollection("attachments.files").find({}, { filename: 1, length: 1, metadata: 1 });

// Скачивание: openDownloadStream → запись в файл на стороне приложения
const fileDoc = db.getCollection("attachments.files").findOne({ filename: "report.pdf" });
const download = bucket.openDownloadStream(fileDoc._id);
