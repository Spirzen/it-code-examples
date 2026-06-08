int process_file(const char *path)
{
    int ret = -1;
    FILE *f = NULL;
    char *buf = NULL;

    f = fopen(path, "r");
    if (f == NULL)
        goto cleanup;

    buf = malloc(4096);
    if (buf == NULL)
        goto cleanup;

    /* ... работа ... */
    ret = 0;

cleanup:
    free(buf);
    if (f != NULL)
        fclose(f);
    return ret;
}
