int up = (rank > 0) ? rank - 1 : MPI_PROC_NULL;
int down = (rank < size - 1) ? rank + 1 : MPI_PROC_NULL;

MPI_Sendrecv(&local[1], nx, MPI_DOUBLE, up, 0,
             &ghost_top, nx, MPI_DOUBLE, up, 1, comm, &st);
MPI_Sendrecv(&local[nlocal], nx, MPI_DOUBLE, down, 1,
             &ghost_bot, nx, MPI_DOUBLE, down, 0, comm, &st);

#pragma omp parallel for
for (int j = 1; j <= nlocal; ++j)
    update_stencil(j);
