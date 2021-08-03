import PySimpleGUI as sg

import agregarGasto
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
    layout= [[sg.Text("PROGRAMA DE GESTION DE GASTOS", size=(30,1), font=("Sawasdee", 25), justification= 'center')],
        
            [sg.Button('Agregar gasto',key = '-agregar-')],
            [sg.Button('salir')]

            ]   
            

    window = sg.Window('proyecto').Layout(layout)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        print(event)
        print(values)


        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        #Si el user clickea agregar gasto debe dirigir el programa a la ventana de agregar gastos
        if event == "-agregar-":
            
            window.hide()

            agregarGasto.start()

            window.un_hide()
            
            

    return window
