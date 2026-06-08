package com.example.app;

import com.example.bean.User;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) {
        
        // Создание экземпляра с использованием конструктора по умолчанию
        User user1 = new User();
        user1.setName("Алексей");
        user1.setAge(30);
        user1.setActive(true);

        System.out.println(user1.toString());

        // Создание экземпляра с использованием конструктора параметров
        User user2 = new User("Мария", 25, true);
        System.out.println(user2.toString());

        // Работа со списком пользователей
        List<User> users = new ArrayList<>();
        users.add(user1);
        users.add(user2);

        // Поиск активного пользователя
        for (User user : users) {
            if (user.isActive()) {
                System.out.println("Активный пользователь: " + user.getName());
            }
        }

        // Пример сериализции и десериализции
        try {
            saveUserToFile(user1, "user_data.ser");
            User restoredUser = loadUserFromFile("user_data.ser");
            System.out.println("Восстановленный пользователь: " + restoredUser);
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Ошибка при работе с файлом: " + e.getMessage());
        }
    }

    // Метод сохранения объекта в файл
    private static void saveUserToFile(User user, String filename) throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(user);
        }
    }

    // Метод загрузки объекта из файла
    private static User loadUserFromFile(String filename) throws IOException, ClassNotFoundException {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
            return (User) ois.readObject();
        }
    }
}
