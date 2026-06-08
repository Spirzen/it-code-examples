#include <errno.h>
#include <limits.h>
#include <stdlib.h>

int parse_int(const char *s, int *out)
{
    char *end = NULL;
    long v;

    if (s == NULL || out == NULL)
        return -1;

    errno = 0;
    v = strtol(s, &end, 10);
    if (errno != 0 || end == s || *end != '\0' || v < INT_MIN || v > INT_MAX)
        return -1;

    *out = (int)v;
    return 0;
}
