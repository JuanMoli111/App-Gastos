import PySimpleGUI as sg

from ventanas.agregarDatos.agregarUsuario import build

from funciones import *

def start(usuarios):

    """
        lanza la ejecucion de la ventana agregarGasto
    """

    window = loop(usuarios)

    window.close()


def loop(usuarios):

    window = build(usuarios)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()


        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        if ((event == '-agregar-') and (values['-usuario-'] != '')):
            
            print(usuarios)

            print(event)


            usuarios.append(values['-usuario-'])

            window['-lista_usuarios-'].update(usuarios)


        
    return window