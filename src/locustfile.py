from locust import TaskSet, task
from locust import HttpUser
import os

# Cada classe aqui declarada é uma API que deve ser chamada
PROPERTIES_PORT = os.getenv("PROPERTIES_PORT", 5005)

class Properties(HttpUser):
    min_wait = 0
    max_wait = 1000

    # Cada task é uma chamada dentro da API escolhida
    # Se for realizada autenticação, pode ser passada
    # como parâmetro dentro do data da requisição
    @task
    def health(self):
        health_url = f"{self.host}:{PROPERTIES_PORT}/api/v1/health"

        self.client.get(health_url, name="properties-health")

    @task(1)
    def insert(self):
        health_url = f"{self.host}:{PROPERTIES_PORT}/api/v1/insert"

        headers = {
           'Content-Type': 'application/json'
        }
        # Se for feita autenticação antes, pasar o token dentro do data
        data = {
            "santos_token":"abcd1234",
            "farmName":"Fazenda encanto",
            "ownerName":"Roberto",
            "car":"PI-2211209-344301157FAE4482A2884266E088DC59"
        }

        self.client.post(health_url, headers=headers, data=data,
                         timeout=60000, name="properties-insert")


### API RESERVA LEGAL MAIS
RESERVALEGALMAIS_PORT = os.getenv("RESERVALEGALMAIS_PORT", 5004)
class ReservaLegalMais(HttpUser):
    min_wait = 0
    max_wait = 1000

    @task
    def health(self):
        self.client.get("/api/v1/health", name="reservalegal-health")