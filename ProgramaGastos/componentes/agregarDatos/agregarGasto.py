import PySimpleGUI as sg

from ventanas.agregarDatos.agregarGasto import build

from funciones import *

def start():

    """
        lanza la ejecucion de la ventana agregarGasto
    """

    window = loop()

    window.close()


def loop():

    ##Decodificar data, necesito los users y los tipos
    data = decode_json()

    #Usuarios_json sera una lista de diccionarios, cada uno representa un gasto
    #usuarios_json = data['usuarios']
    #tipos_json = data['tipos']

    #Pasarle los users y los tipos al window BUILD
    window = build(data['usuarios'],data['tipos'])


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        if event == "aceptar":

            gastos_json = data['gastos']

            #Crea un diccionario gasto para almacenar los datos del gasto, recibido en los elementos de la pantalla
            gasto = {
                'monto' : values['-monto-'],
                'fecha' : [values['-dia-'] + '/' + values['-mes-'] + '/' + values['-anio-']],
                'peso'  : values['-peso-'],
                'tipo'  : values['-tipo-'],
                'comprador': values['-autor-'],

                #el codigo unico de cada gasto asignado como el tamaño actual de la lista de gastos mas uno
                'codigo': str(len(gastos_json) + 1)

            }

            #Agrega el dicc a la lista de diccionarios 
            gastos_json.append(gasto)
            
            #Sobreescribe el json con la nueva lista
            write_json(data)
            

    return window
