import PySimpleGUI as sg


import time as t

from ventanas.menu import build

from componentes.agregarDatos.agregarGasto import start as AgregarGastoStart

from componentes.visualizarDatos import start as VisualizarDatosStart

from componentes.AgregarDatos import start as AgregarDatosStart

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
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","Salir"):
            break

        #Si el user clickea agregar gasto debe dirigir el programa a la ventana de agregar gastos
        if event == "-agregar-":
            
            window.hide()

            #Moverse a la ventana de agregar gastos
            AgregarDatosStart()

            window.un_hide()

        #Si el user clickea visualizar gasto debe dirigir el programa a la ventana de visualizar gastos
        if event == "-visualizar-":
            
            window.hide()

            #Moverse a la ventana de visualizar gastos
            VisualizarDatosStart()

            window.un_hide()
             
        #Si el user clickea eliminar gasto debe dirigir el programa a la ventana de eliminar gastos
        
        if event == "-eliminar-":
            
            window.hide()

            #Moverse a la ventana de eliminar gastos
            #EliminarGastoStart()

            window.un_hide()       
                        
            

    return window
