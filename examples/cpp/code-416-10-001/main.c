sem_t empty, full;
pthread_mutex_t buf_mutex;

sem_wait(&empty);
pthread_mutex_lock(&buf_mutex);
  push(item);
pthread_mutex_unlock(&buf_mutex);
sem_post(&full);
