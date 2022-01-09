import PySimpleGUI as sg

from ventanas.agregarDatos.agregarTipo import build


from funciones import *

def start(tipos):

    """
        lanza la ejecucion de la ventana agregarGasto
    """

    window = loop(tipos)

    window.close()


def loop(tipos):

    window = build(tipos)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        if ((event == '-agregar-') and (values['-tipo-'] != '')):
            

            tipos.append(values['-usuario-'])

            window['-lista_usuarios-'].update(tipos)



    return window