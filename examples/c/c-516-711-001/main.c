int attempts = 0;
int max_attempts = 7;
int guess;

while (attempts < max_attempts) {
    printf("Введите ваше число: ");
    scanf("%d", &guess);
    attempts++;

    if (guess == secret) {
        printf("Поздравляем! Вы угадали число за %d попыток.\n", attempts);
        break;
    } else if (guess < secret) {
        printf("Слишком мало!\n");
    } else {
        printf("Слишком много!\n");
    }
}

if (attempts >= max_attempts && guess != secret) {
    printf("Вы исчерпали все попытки. Загаданное число было: %d\n", secret);
}
