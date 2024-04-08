import json
import os
import PIL.Image
import io
import base64
from datetime import datetime

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

def ConvertirEnFloatTruncado(num):
    """
        Recibe un numero y lo convierte en un float con dos decimales, ya sea que reciba un float, un integer, o un string
        si recibe un string vacio devuelve 0.   Si recibe un String representando un numero decimal con ',' lo convierte en '.'
    """

    if (isinstance(num,str)):
        if(num == ''):
            return 0
        else:
                num = float(num.replace(",","."))

    return float("{:.2f}".format(num))
    
def ordenarGastosPorFecha(lista_gastos):
    
   return sorted(lista_gastos, key=lambda date: datetime.strptime(date['fecha'], '%d-%m-%Y'))

def binary_search_insert(gastos, nuevo_gasto):
    fecha_nuevo_gasto = datetime.strptime(nuevo_gasto['fecha'], '%d-%m-%Y')
    low = 0
    high = len(gastos)
    while low < high:
        mid = (low + high) // 2
        mid_fecha = datetime.strptime(gastos[mid]['fecha'], '%d-%m-%Y')
        if mid_fecha < fecha_nuevo_gasto:
            low = mid + 1
        else:
            high = mid
    gastos.insert(low, nuevo_gasto)

def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()


def filter_lista(input_string,lista,min_substring_length_filter):
    input_string_lower = input_string.lower()

    if len(input_string_lower) < min_substring_length_filter:
        return lista

    matches = []

    for item in lista:
        item_lower = item.lower()
        match_count = 0
        matching_substrings = set()

        for i in range(len(input_string_lower) - (min_substring_length_filter - 1)):
            substring = input_string_lower[i:i + min_substring_length_filter] 
            if substring in item_lower:
                match_count += 1
                matching_substrings.add(substring)

        if match_count > 0:
            matches.append((item, match_count, sorted(matching_substrings)))

    
    matches.sort(key=lambda x: (x[1], x[0]), reverse=True)

    return [match[0] for match in matches]



#Definimos la variable path en el mismo modulo que las funciones que lo usan
path = forzar_path()