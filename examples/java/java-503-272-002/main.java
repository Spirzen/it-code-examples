package com.example.demo.web;

import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class ApiController {

    @GetMapping("/api/public")
    public Map<String, String> publicEndpoint() {
        return Map.of("message", "ok");
    }

    @GetMapping("/api/private")
    public Map<String, String> privateEndpoint(@AuthenticationPrincipal UserDetails user) {
        return Map.of("message", "hello, " + user.getUsername());
    }
}
