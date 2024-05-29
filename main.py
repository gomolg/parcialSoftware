from controllers.controller import Agenda


def main():
    uri = "mongodb+srv://gomolg:hola1234@clusteruao.xtakili.mongodb.net"
    agenda = Agenda(uri)
    agenda.ejecutar()  # Delegar la ejecución y la lógica al método ejecutar del controlador


if __name__ == "__main__":
    main()
