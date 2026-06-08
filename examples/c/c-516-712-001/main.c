#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define BUFFER_SIZE 4096

int main(int argc, char *argv[]) {
    if (argc != 3) return 1;

    int src = open(argv[1], O_RDONLY);
    if (src == -1) return 1;

    int dst = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    if (dst == -1) {
        close(src);
        return 1;
    }

    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;
    while ((bytes_read = read(src, buffer, BUFFER_SIZE)) > 0) {
        write(dst, buffer, bytes_read);
    }

    close(src);
    close(dst);
    return 0;
}
