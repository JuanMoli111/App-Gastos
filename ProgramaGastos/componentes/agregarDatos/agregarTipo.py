import PySimpleGUI as sg

from ventanas.AgregarDatos.agregarTipo import build


from funciones import *

def start():

    """
        lanza la ejecucion de la ventana agregarGasto
    """

    window = loop()

    window.close()


def loop():
    
    #Decodifica los datos del json en una estructura de datos 
    data = decode_json()

    lista_tipos = data['tipos']
    window = build(lista_tipos)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        ##Si clickeo agregar y el input no es vacio
        if ((event == '-agregar-') and (values['-tipo-'] != '')):

            #MODULARIZAR
            #Crea un diccionario gasto para almacenar los datos del tipo, recibido en los elementos de la pantalla
            tipo = values['-tipo-']
            
            #Agrega el dicc a la lista de diccionarios 
            lista_tipos.append(tipo)
            
            #Sobreescribe el json con la nueva lista
            write_json(data)

            window['-lista_tipos-'].update(lista_tipos)



    return window