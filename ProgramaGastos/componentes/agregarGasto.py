import PySimpleGUI as sg

from ventanas.agregarGasto import build

from funciones import *

def start():

    """
        lanza la ejecucion de la ventana agregarGasto
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

            #Gastos_json sera una lista de diccionarios, cada uno representa un gasto
            gastos_json = data['gastos']


            #Crea un diccionario gasto para almacenar los datos del gasto, recibido en los elementos de la pantalla
            gasto = {

                'monto' : values['-monto-'],
                'fecha' : [values['-dia-'] + '/' + values['-mes-'] + '/' + values['-anio-']],
                'tipo'  : values['-tipo-'],

                'comprador': values['-autor-']


            }

            #Agrega el dicc a la lista de diccionarios 
            gastos_json.append(gasto)

            
            #Sobreescribe el json con la nueva lista
            write_json(data)
            

    return window
