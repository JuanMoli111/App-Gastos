from funciones import decode_json
import PySimpleGUI as sg

from ventanas.visualizarDatos import build


def start():

    """
    Lanza la ejecución de la primer ventana
    """
    window = loop()

    window.close()

def loop():

    #Decodifica el json para recuperar la informacion
    data = decode_json()

    lista_gastos = data["gastos"]

    window = build(lista_gastos)

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","Salir"):
            break



    return window