import PySimpleGUI as sg


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


## BUILD DE LA VENTANA

def build():
    """
    build de la ventana para el menu agregar datos, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """


    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Necesitamos tres botones para cada tipo de dato a agregar, 

    layout = [

        ##Botones para acceder a las ventanas para agregar cada tipo de dato
        [sg.Button('Agregar gastos', key = '-gasto-')],
        [sg.Button('Agregar tipos de producto', key = '-tipo-')],
        [sg.Button('Agregar usuarios', key = '-usuario-')],

        ##Boton salir
        [sg.Button('Salir', key = 'salir')]

    ]

    ##Retorna un objeto Window que crea pasandole el layout creado
    return sg.Window(title = "Menu - Agregar datos", layout = layout, margins = (100,100))
