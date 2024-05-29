# tests/test_contacto.py
from models.contacto import Contacto


def test_crear_contacto():
    contacto = Contacto("Juan Pérez", "1234567890", "juan@example.com")
    assert contacto.nombre == "Juan Pérez"
    assert contacto.telefono == "1234567890"
    assert contacto.email == "juan@example.com"
