func upload(c *gin.Context) {
    file, err := c.FormFile("document")
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "file required"})
        return
    }
    dst := filepath.Join(os.TempDir(), filepath.Base(file.Filename))
    if err := c.SaveUploadedFile(file, dst); err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "save failed"})
        return
    }
    c.JSON(http.StatusCreated, gin.H{"path": dst})
}

func download(c *gin.Context) {
    c.FileAttachment("/data/report.pdf", "report.pdf")
}
