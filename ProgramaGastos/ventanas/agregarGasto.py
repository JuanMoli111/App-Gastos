import PySimpleGUI as sg

from funciones import *

def start():

    """
    Lanza la ejecución de la primer ventana
    """

    window = loop()

    window.close()


def loop():
    """
    Loop de la ventana de menú inicio que capta los eventos al apretar las opciones
    """

    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado

    layout= [[sg.Text('Agregar gasto', size=(30,1), font=("Sawasdee", 25), justification= 'center')],

            [sg.Text('Monto'),sg.Input(key='-monto-')],   
            [[sg.Text('Dia'),sg.Input(key='-dia-')],[sg.Text('Mes'),sg.Input(key='-mes-')],[sg.Text('Año'),sg.Input(key='-anio-')]],   
            [sg.Text('Tipo de gasto'),sg.Input(key='-tipo-')],          
            [sg.Button('aceptar'),sg.Button('salir')]

            ]   

    window = sg.Window(title = "Hello World", layout = layout, margins = (400,200))

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        print(event)
        print(values)


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
