const int threshold = 64;
for (int k = 0; k < n; ++k) {
    normalize_pivot_row(k);  // одна строка — последовательно
    int rows_left = n - k - 1;
    if (rows_left >= threshold) {
#pragma omp parallel for schedule(dynamic, 8)
        for (int i = k + 1; i < n; ++i)
            eliminate_row(i, k);
    } else {
        for (int i = k + 1; i < n; ++i)
            eliminate_row(i, k);
    }
}
