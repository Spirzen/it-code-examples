package com.example.demo.model;

import lombok.Data;

@Data
public class Greeting {
    private String message;
    private String name;

    public Greeting() {
        this.message = "Привет";
        this.name = "Мир";
    }

    public Greeting(String name) {
        this.message = "Привет";
        this.name = name;
    }

    public String getMessage() {
        return message + ", " + name + "!";
    }
}
