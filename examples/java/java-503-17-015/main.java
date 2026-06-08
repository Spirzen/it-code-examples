Scanner scanner = new Scanner(System.in);
int choice;
do {
    System.out.println("Меню:");
    System.out.println("1. Показать баланс");
    System.out.println("2. Пополнить счёт");
    System.out.println("3. Выйти");
    System.out.print("Выберите действие: ");
    choice = scanner.nextInt();
    
    switch (choice) {
        case 1 -> System.out.println("Баланс: 1000 руб.");
        case 2 -> System.out.println("Счёт пополнен");
        case 3 -> System.out.println("Выход");
        default -> System.out.println("Неверный выбор");
    }
} while (choice != 3);
scanner.close();
