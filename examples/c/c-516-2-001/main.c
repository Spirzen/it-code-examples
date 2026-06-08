int *zeros = calloc(10, sizeof(int));
if (zeros == NULL) {
    return 1;
}

zeros[0] = 42; /* остальные элементы уже равны 0 */

int *bigger = realloc(zeros, 20 * sizeof(int));
if (bigger == NULL) {
    free(zeros);
    return 1;
}
zeros = bigger;

free(zeros);
zeros = NULL;
