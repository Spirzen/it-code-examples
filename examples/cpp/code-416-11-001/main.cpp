#include <omp.h>

void saxpy(int n, double a, const double* x, double* y) {
#pragma omp parallel for
    for (int i = 0; i < n; ++i)
        y[i] = a * x[i] + y[i];
}
