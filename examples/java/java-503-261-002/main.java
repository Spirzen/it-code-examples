package com.example.bean;

import java.io.Serializable;

public class User implements Serializable {
    
    private static final long serialVersionUID = 1L;
    
    // Приватные поля (свойства)
    private String name;
    private int age;
    private boolean active;

    // Публичный конструктор без аргументов (обязательно для JavaBeans)
    public User() {
        this.name = "";
        this.age = 0;
        this.active = false;
    }

    // Конструктор с параметрами для удобства инициализации
    public User(String name, int age, boolean active) {
        this.name = name;
        this.age = age;
        this.active = active;
    }

    // Геттеры и сеттеры для свойства 'name'
    public String getName() {
        return name;
    }

    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name.trim();
        } else {
            throw new IllegalArgumentException("Имя не может быть пустым");
        }
    }

    // Геттеры и сеттеры для свойства 'age'
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age >= 0 && age <= 150) {
            this.age = age;
        } else {
            throw new IllegalArgumentException("Некорректный возраст");
        }
    }

    // Геттеры и сеттеры для свойства 'active'
    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    // Метод для получения полной информации о пользователе
    @Override
    public String toString() {
        return String.format("User{name='%s', age=%d, active=%b}", name, age, active);
    }
}
