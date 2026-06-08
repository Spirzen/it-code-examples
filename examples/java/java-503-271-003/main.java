package com.example.demo.service;

import com.example.demo.model.Greeting;
import org.springframework.stereotype.Service;

@Service
public class GreetingService {

    public Greeting createGreeting(String name) {
        if (name == null || name.trim().isEmpty()) {
            return new Greeting("Гость");
        }
        return new Greeting(name.trim());
    }
}
