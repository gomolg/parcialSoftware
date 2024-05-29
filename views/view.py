# views/view.py

def mostrar_menu():
    print("\nAgenda Telefónica")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Listar contactos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def obtener_datos_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    email = input("Ingrese el email del contacto: ")
    return nombre, telefono, email


def obtener_nombre_busqueda():
    return input("Ingrese el nombre del contacto para buscar o eliminar: ")


def mostrar_mensaje(mensaje):
    print(mensaje)
