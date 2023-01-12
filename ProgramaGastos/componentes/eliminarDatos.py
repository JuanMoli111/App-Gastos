from funciones import decode_json

import PySimpleGUI as sg

from ventanas.eliminarDatos import build


def start():

    """
    Lanza la ejecución de la primer ventana
    """
    window = loop()

    window.close()

def loop():

    #Decodifica el json para recuperar la informacion (Si decodifico el JSON en el loop event, y lo envia a la ventana, sería esta la forma de actualziar la informacion mientras se introduce?)
    data = decode_json()

    lista_gastos = data["gastos"]
    lista_usuarios = data["usuarios"]
    lista_tipos = data["tipos"]

    window = build(lista_gastos,lista_usuarios,lista_tipos)

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break



    return window