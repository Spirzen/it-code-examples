package com.example.bean;

import jakarta.annotation.PostConstruct;
import jakarta.faces.application.FacesMessage;
import jakarta.faces.context.FacesContext;
import jakarta.inject.Named;
import java.io.Serializable;

@Named("counterBean")
@RequestScoped
public class CounterBean implements Serializable {
    
    private static final long serialVersionUID = 1L;
    
    private int count;
    private String name;
    private String message;

    @PostConstruct
    public void init() {
        this.count = 0;
        this.name = "";
        this.message = "Добро пожаловать!";
    }

    public void increment() {
        count++;
    }

    public void decrement() {
        if (count > 0) {
            count--;
        }
    }

    public void reset() {
        count = 0;
        message = "Счетчик сброшен.";
    }

    public void validateName(FacesContext context) {
        if (name == null || name.trim().isEmpty()) {
            context.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR, 
                "Ошибка", "Имя не может быть пустым"));
        } else {
            message = "Привет, " + name + "!";
        }
    }

    // Геттеры и сеттеры
    public int getCount() { return count; }
    public void setCount(int count) { this.count = count; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
}
