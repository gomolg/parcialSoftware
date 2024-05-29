import pytest
from controllers.controller import Agenda



@pytest.fixture
def agenda():
    # Configurar una conexión a una base de datos de prueba
    uri = "mongodb+srv://gomolg:hola1234@clusteruao.xtakili.mongodb.net/test_agenda"
    # Limpiar la base de datos antes de cada prueba
    agenda = Agenda(uri)
    agenda.modelo.contactos.delete_many({})
    return agenda


def test_agregar_contacto(agenda):
    nombre = "Juan Perez"
    telefono = "1234567890"
    email = "juan.perez@example.com"

    agenda.modelo.agregar_contacto(nombre, telefono, email)
    contacto = agenda.modelo.buscar_contacto(nombre)

    assert contacto is not None
    assert contacto['nombre'] == nombre
    assert contacto['telefono'] == telefono
    assert contacto['email'] == email


def test_eliminar_contacto(agenda):
    nombre = "Juan Perez"
    telefono = "1234567890"
    email = "juan.perez@example.com"

    agenda.modelo.agregar_contacto(nombre, telefono, email)
    agenda.modelo.eliminar_contacto(nombre)
    contacto = agenda.modelo.buscar_contacto(nombre)

    assert contacto is None


def test_buscar_contacto_existente(agenda):
    nombre = "Juan Perez"
    telefono = "1234567890"
    email = "juan.perez@example.com"

    agenda.modelo.agregar_contacto(nombre, telefono, email)
    contacto = agenda.modelo.buscar_contacto(nombre)

    assert contacto is not None
    assert contacto['nombre'] == nombre
    assert contacto['telefono'] == telefono
    assert contacto['email'] == email


def test_buscar_contacto_inexistente(agenda):
    nombre = "Juan Perez"

    contacto = agenda.modelo.buscar_contacto(nombre)

    assert contacto is None