pub struct LoggingWriter<W: Write> {
    inner: W,
    label: String,
}

impl<W: Write> LoggingWriter<W> {
    pub fn new(inner: W, label: &str) -> Self {
        Self {
            inner,
            label: label.to_string(),
        }
    }
}

impl<W: Write> Write for LoggingWriter<W> {
    fn write(&mut self, buf: &[u8]) -> std::io::Result<usize> {
        println!("[{}] Writing {} bytes", self.label, buf.len());
        self.inner.write(buf)
    }
    
    fn flush(&mut self) -> std::io::Result<()> {
        self.inner.flush()
    }
}
