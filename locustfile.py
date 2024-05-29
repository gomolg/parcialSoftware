from locust import HttpUser, task, between


class AgendaTelefonicaUser(HttpUser):
    wait_time = between(1, 5)  # Simula un tiempo de espera entre tareas de 1 a 5 segundos.

    @task
    def agregar_contacto(self):
        self.client.post("/agregar", json={"nombre": "Test", "telefono": "1234567890", "email": "test@example.com"})

    @task
    def listar_contactos(self):
        self.client.get("/listar")

    @task
    def buscar_contacto(self):
        self.client.get("/buscar?nombre=Test")

# Asume que tus endpoints son /agregar, /listar, /buscar
