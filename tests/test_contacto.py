# tests/test_contacto.py
from models.contacto import ContactoModel
from pymongo import MongoClient
import pytest


# Reemplaza 'your_mongo_uri' con tu URI de MongoDB real para la prueba
@pytest.fixture
def contacto_model():
    return ContactoModel("mongodb+srv://gomolg:hola1234@clusteruao.xtakili.mongodb.net")


def test_crear_contacto(contacto_model):
    contacto_model.agregar_contacto("Juan Pérez", "1234567890", "juan@example.com")
    contacto = contacto_model.buscar_contacto("Juan Pérez")

    assert contacto is not None
    assert contacto['nombre'] == "Juan Pérez"
    assert contacto['telefono'] == "1234567890"
    assert contacto['email'] == "juan@example.com"
