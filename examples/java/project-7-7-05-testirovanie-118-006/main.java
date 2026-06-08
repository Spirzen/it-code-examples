package com.example.api.tests;

import static io.restassured.RestAssured.given;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import org.junit.jupiter.api.Test;

public class UserServiceApiTest {

    @Test
    public void testGetUserById() {
        given()
            .baseUri("https://api.example.com")
            .pathParam("id", "123")
        .when()
            .get("/users/{id}")
        .then()
            .statusCode(200)
            .body("name", equalTo("Ivan Petrov"))
            .body("email", containsString("@example.com"));
    }
}
