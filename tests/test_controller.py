# tests/test_controller.py
import pytest
from controllers.controller import Agenda


@pytest.fixture
def agenda():
    # Configurar una conexión a una base de datos de prueba
    uri = "mongodb+srv://felipemolina:admin@edya2.zgsyghc.mongodb.net"
    return Agenda(uri)


def test_agregar_contacto(agenda):
    resultado = agenda.agregar_contacto("Ana López", "0987654321", "ana@example.com")
    assert "Contacto agregado con ID:" in resultado


def test_buscar_contacto_existente(agenda):
    # Asumiendo que ya has agregado este contacto como parte de una configuración inicial o usando fixtures
    agenda.agregar_contacto("Carlos Mora", "222333444", "carlos@example.com")
    resultado = agenda.buscar_contacto("Carlos Mora")
    assert resultado == "Carlos Mora, 222333444, carlos@example.com"


def test_buscar_contacto_inexistente(agenda):
    resultado = agenda.buscar_contacto("Nadie Nadie")
    assert resultado == "Contacto no encontrado."


def test_eliminar_contacto_existente(agenda):
    # Añadir un contacto para luego eliminarlo
    agenda.agregar_contacto("Laura Gómez", "555666777", "laura@example.com")
    resultado = agenda.eliminar_contacto("Laura Gómez")
    assert resultado == "Contacto eliminado."


def test_eliminar_contacto_inexistente(agenda):
    resultado = agenda.eliminar_contacto("Persona Ficticia")
    assert resultado == "Contacto no encontrado."


def test_listar_contactos_con_datos(agenda):
    # Limpiar la base de datos primero si es necesario
    agenda.agregar_contacto("Sofía Cruz", "888999000", "sofia@example.com")
    resultado = agenda.listar_contactos()
    expected_output = "Sofía Cruz, 888999000, sofia@example.com"
    assert expected_output in resultado
# Más pruebas pueden ser añadidas aquí
