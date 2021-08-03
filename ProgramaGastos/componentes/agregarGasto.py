import PySimpleGUI as sg

from ventanas.agregarGasto import build
from funciones import *

def start():

    """
    Lanza la ejecución de la primer ventana
    """

    window = loop()

    window.close()


def loop():

    window = build()


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        if event == "aceptar":

            #Decodifica los datos del json en una estructura de datos 
            data = decode_json()

            #Gastos sea una lista de diccionarios cada uno representa un gasto
            gastos_json = data['gastos']

            print(type(gastos_json))

            gasto = {

                'monto' : values['-monto-'],
                'fecha' : [values['-dia-'],values['-mes-'],values['-anio-']],
                'tipo'  : values['-tipo-']
                
            }

            gastos_json.append(gasto)

            #monto = values['-monto-']

            write_json(data)
            

    return window
