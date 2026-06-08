#include <pthread.h>
#include <stdio.h>

static int shared = 0;
static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void *worker(void *arg)
{
  (void)arg;
  for (int i = 0; i < 100000; i++) {
    pthread_mutex_lock(&lock);
    shared++;
    pthread_mutex_unlock(&lock);
  }
  return NULL;
}

int main(void)
{
  pthread_t t1, t2;
  pthread_create(&t1, NULL, worker, NULL);
  pthread_create(&t2, NULL, worker, NULL);
  pthread_join(t1, NULL);
  pthread_join(t2, NULL);
  printf("shared=%d\n", shared); /* ожидаем 200000 */
  return 0;
}
