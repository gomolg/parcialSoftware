from pymongo import MongoClient


class ContactoModel:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['agenda_telefonica']
        self.contactos = self.db.contactos

    def agregar_contacto(self, nombre, telefono, email):
        nuevo_contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
        return self.contactos.insert_one(nuevo_contacto)

    def buscar_contacto(self, nombre):
        return self.contactos.find_one({'nombre': nombre})

    def eliminar_contacto(self, nombre):
        return self.contactos.delete_one({'nombre': nombre})

    def listar_contactos(self):
        return list(self.contactos.find())
