from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Время паузы между действиями пользователя (от 1 до 3 секунд)
    wait_time = between(1, 3)

    @task(3)
    def index_page(self):
        # Загрузка главной страницы с частотой 3 раза больше других задач
        self.client.get("/")

    @task(1)
    def get_about_page(self):
        # Загрузка страницы "О нас"
        self.client.get("/about")

    @task
    def create_account(self):
        # Создание аккаунта с передачей данных в теле запроса
        self.client.post("/login", json={"username": "test_user", "password": "secret"})
