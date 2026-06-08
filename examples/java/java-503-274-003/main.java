package com.example.demo.web;

import org.springframework.http.ResponseEntity;
import org.springframework.security.oauth2.jwt.JwtClaimsSet;
import org.springframework.security.oauth2.jwt.JwtEncoder;
import org.springframework.security.oauth2.jwt.JwtEncoderParameters;
import org.springframework.web.bind.annotation.*;

import java.time.Instant;
import java.util.Map;

record LoginRequest(String username, String password) {}
record TokenResponse(String accessToken, String tokenType, long expiresIn) {}

@RestController
@RequestMapping("/auth")
public class AuthController {

    private final JwtEncoder jwtEncoder;

    public AuthController(JwtEncoder jwtEncoder) {
        this.jwtEncoder = jwtEncoder;
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest req) {
        if (!"demo".equals(req.username()) || !"secret".equals(req.password())) {
            return ResponseEntity.status(401).body(Map.of("error", "invalid credentials"));
        }

        Instant now = Instant.now();
        JwtClaimsSet claims = JwtClaimsSet.builder()
            .issuer("demo-app")
            .subject(req.username())
            .issuedAt(now)
            .expiresAt(now.plusSeconds(3600))
            .claim("scope", "read")
            .build();

        var jwt = jwtEncoder.encode(JwtEncoderParameters.from(claims));
        return ResponseEntity.ok(new TokenResponse(jwt.getTokenValue(), "Bearer", 3600));
    }
}
