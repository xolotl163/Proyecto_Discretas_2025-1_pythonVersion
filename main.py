
# Importar las clases necesarias

from behavioral.Controller import Controller as Controller

def main():

    controller00 = Controller()
    controller00.initialize_data()
    controller00.set_id_controller("Controller 00")
    controller00.set_controller_number(1)

    message1 = "\nIngresa el nombre de la estacion de inicio\n"
    message2 = "\nIngresa el nombre de la estacion de llegada\n"
    message3 = "\nQuieres realizar otra busqueda? 1.- si 0.- no\n"
    flag = 1

    while flag == 1:

        start = input(message1)
        end = input(message2)


        path = controller00.find_path(
            controller00.find_node(start),
            controller00.find_node(end)
        )

        if path:
            for station in reversed(path):
                print(station.get_id(), end=" -> ")
            print("End")

        flag = int( input(message3) )

    print("---> Fin del programa <---")

if __name__ == "__main__":
    main()