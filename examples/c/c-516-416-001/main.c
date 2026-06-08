#include <stdio.h>
#include <time.h>

FILE *log = fopen("app.log", "a");
if (log == NULL) {
    perror("app.log");
    return 1;
}

if (fprintf(log, "[%ld] started\n", (long)time(NULL)) < 0) {
    perror("write");
    fclose(log);
    return 1;
}

fclose(log);
