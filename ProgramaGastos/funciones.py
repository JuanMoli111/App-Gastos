import json
import os


def write_json(data):
    """esta funcion reescribe el json con el parámetro data"""

    #Sobreescribe el json con la informacion actualizada, que debe recibirse en data
    with open(path,'w') as f:
        json.dump(data, f, indent=4)


def decode_json():

    """esta funcion convierte el json en una estructura de datos y la retorna"""

    #en este caso data será un diccionario con la lista de diccionarios del json
    with open(path,"r") as json_file:
        data = json.load(json_file)

    return data


def forzar_path():
    """Esta funcion define una variable path con el directorio del json y la retorna
       Si el json no existe lo crea.
    """

    #Crea un string con el path donde deberia estar el json, el directorio se crea dinámicamente (funciona en todos los S.O)
    path = os.path.join(os.getcwd(),'gastos.json')

    #Si el path no es valido, significa que el json no está, debemos crearlo antes de solicitar los datos del gasto
    if not(os.path.exists(path)):

        #Creamos el diccionario para los gastos
        temp = {}

        temp['gastos'] = []


        #Creamos el archivo json, almacenamos la lista vacía de gastos

        with open('gastos.json',"x") as json_file:
            json.dump(temp, json_file, indent=4)


    return path

#Definimos la variable path en el mismo modulo que las funciones que lo usan
path = forzar_path()