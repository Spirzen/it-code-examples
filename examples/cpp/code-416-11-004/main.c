#include <mpi.h>
#include <math.h>

void gauss_step_k(int k, int n, double *A, double *b,
                  int rank, int owner_k) {
    int pivot_row = k;
    if (rank == owner_k) {
        double max_val = fabs(A[k * n + k]);
        pivot_row = k;
        for (int i = k + 1; i < n; ++i) {
            double v = fabs(A[i * n + k]);
            if (v > max_val) { max_val = v; pivot_row = i; }
        }
    }
    MPI_Bcast(&pivot_row, 1, MPI_INT, owner_k, MPI_COMM_WORLD);

    /* swap_rows_if_needed(k, pivot_row) — зависит от разбиения */

    int row_len = n - k + 1;   /* A[k,k..n-1] и b[k] */
    double *row_buf = NULL;
    if (rank == owner_k) {
        row_buf = malloc(row_len * sizeof(double));
        for (int j = k; j < n; ++j)
            row_buf[j - k] = A[k * n + j] / A[k * n + k];
        row_buf[n - k] = b[k] / A[k * n + k];
    }
    if (rank != owner_k)
        row_buf = malloc(row_len * sizeof(double));

    MPI_Bcast(row_buf, row_len, MPI_DOUBLE, owner_k, MPI_COMM_WORLD);

    for (int i = k + 1; i < n; ++i) {   /* только строки, локальные на rank */
        double factor = A[i * n + k];
        for (int j = k; j < n; ++j)
            A[i * n + j] -= factor * row_buf[j - k];
        b[i] -= factor * row_buf[n - k];
    }
    free(row_buf);
}
