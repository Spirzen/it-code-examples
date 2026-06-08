ssize_t n = read(src, buffer, sizeof buffer);
if (n < 0) {
    perror("read");
    close(src);
    close(dst);
    return 1;
}
if (n == 0)
    break; /* конец файла */

if (write(dst, buffer, (size_t)n) != n) {
    perror("write");
    close(src);
    close(dst);
    return 1;
}
