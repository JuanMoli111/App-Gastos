import PySimpleGUI as sg

from ventanas.menuAgregarDatos import build

from componentes.AgregarDatos.agregarGasto import start as AgregarGastoStart

from componentes.AgregarDatos.agregarTipo import start as AgregarTipoStart

from componentes.AgregarDatos.agregarUsuario import start as AgregarUsuarioStart

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
        
        #Si el user clickea agregar tipos de productos debe dirigir el programa a la ventana de agregar tipos de productos
        if event == "-tipo-":
            
            window.hide()

            #Moverse a la ventana de agregar tipos
            AgregarTipoStart()

            window.un_hide()
        
        #Si el user clickea agregar usuario debe dirigir el programa a la ventana de agregar usuarios
        if event == "-usuario-":
            
            window.hide()

            #Moverse a la ventana de agregar gastos
            AgregarUsuarioStart()

            window.un_hide()

    return window