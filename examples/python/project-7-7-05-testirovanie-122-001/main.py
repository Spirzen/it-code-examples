   from locust import HttpUser, task, between

   class WebsiteUser(HttpUser):
       host = "https://example.com"
       wait_time = between(1, 3)  # пауза между задачами: 1–3 сек

       @task(3)  # вес 3 — будет вызываться в 3 раза чаще
       def view_product(self):
           product_id = random.randint(1, 1000)
           self.client.get(f"/product/{product_id}", name="/product/[id]")

       @task(1)
       def buy_product(self):
           self.client.post("/cart/add", json={"id": 123, "qty": 1})
           self.client.post("/checkout", json={"payment": "card"})
