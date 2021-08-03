import PySimpleGUI as sg

from ventanas.menu import build
from componentes.agregarGasto import start as AgregarGastoStart

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

        print(event)
        print(values)


        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        #Si el user clickea agregar gasto debe dirigir el programa a la ventana de agregar gastos
        if event == "-agregar-":
            
            window.hide()

            #Moverse a la ventana de agregar gastos
            AgregarGastoStart()

            window.un_hide()
            
            

    return window
