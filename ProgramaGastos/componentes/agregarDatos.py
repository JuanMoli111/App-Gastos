import PySimpleGUI as sg

from ventanas.agregarDatos import build

from componentes.agregarGasto import start as AgregarGastoStart

from funciones import *

def start():

    """
        lanza la ejecucion de la ventana agregarDatos
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

                #Si el user clickea agregar gasto debe dirigir el programa a la ventana de agregar gastos
        if event == "-gasto-":
            
            window.hide()

            #Moverse a la ventana de agregar gastos
            AgregarGastoStart()

            window.un_hide()

    return window