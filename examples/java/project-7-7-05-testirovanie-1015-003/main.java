package api;

import io.restassured.RestAssured;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

class PostsApiTest {

    @BeforeAll
    static void setup() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";
    }

    @Test
    void getPostReturns200AndTitle() {
        given()
            .pathParam("id", 1)
        .when()
            .get("/posts/{id}")
        .then()
            .statusCode(200)
            .body("id", equalTo(1))
            .body("title", not(emptyString()))
            .body("userId", greaterThan(0));
    }

    @Test
    void createPostReturns201() {
        String body = """
            {"title": "QA test", "body": "from REST Assured", "userId": 1}
            """;

        given()
            .header("Content-Type", "application/json")
            .body(body)
        .when()
            .post("/posts")
        .then()
            .statusCode(201)
            .body("title", equalTo("QA test"));
    }
}
