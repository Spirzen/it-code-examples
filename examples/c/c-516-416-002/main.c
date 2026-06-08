#include <stdio.h>

int copy_file(const char *src_path, const char *dst_path)
{
    FILE *in = fopen(src_path, "rb");
    if (in == NULL) {
        perror(src_path);
        return -1;
    }

    FILE *out = fopen(dst_path, "wb");
    if (out == NULL) {
        perror(dst_path);
        fclose(in);
        return -1;
    }

    unsigned char buf[4096];
    size_t n;

    while ((n = fread(buf, 1, sizeof buf, in)) > 0) {
        if (fwrite(buf, 1, n, out) != n) {
            perror("write");
            fclose(in);
            fclose(out);
            return -1;
        }
    }

    if (ferror(in)) {
        perror("read");
        fclose(in);
        fclose(out);
        return -1;
    }

    fclose(in);
    fclose(out);
    return 0;
}
