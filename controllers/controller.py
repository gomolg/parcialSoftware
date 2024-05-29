from models.contacto import ContactoModel
from views.view import mostrar_menu, obtener_datos_contacto, obtener_nombre_busqueda, mostrar_mensaje


class Agenda:
    def __init__(self, uri):
        self.modelo = ContactoModel(uri)

    def ejecutar(self):
        while True:
            opcion = mostrar_menu()
            if opcion == '1':
                nombre, telefono, email = obtener_datos_contacto()
                resultado = self.modelo.agregar_contacto(nombre, telefono, email)
                mostrar_mensaje("Contacto agregado con ID: {}".format(resultado.inserted_id))
            elif opcion == '2':
                nombre = obtener_nombre_busqueda()
                resultado = self.modelo.buscar_contacto(nombre)
                if resultado:
                    mostrar_mensaje("{}, {}, {}".format(resultado['nombre'], resultado['telefono'], resultado['email']))
                else:
                    mostrar_mensaje("Contacto no encontrado.")
            elif opcion == '3':
                nombre = obtener_nombre_busqueda()
                resultado = self.modelo.eliminar_contacto(nombre)
                if resultado.deleted_count > 0:
                    mostrar_mensaje("Contacto eliminado.")
                else:
                    mostrar_mensaje("Contacto no encontrado.")
            elif opcion == '4':
                resultados = self.modelo.listar_contactos()
                if resultados:
                    for contacto in resultados:
                        mostrar_mensaje("{}, {}, {}".format(contacto['nombre'], contacto['telefono'], contacto['email']))
                else:
                    mostrar_mensaje("No hay contactos guardados.")
            elif opcion == '5':
                break
            else:
                mostrar_mensaje("Opción inválida. Por favor, intente de nuevo.")
