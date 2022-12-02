import PySimpleGUI as sg

from funciones import *

from ventanas.agregarDatos.agregarUsuario import build


def start():

    """
        lanza la ejecucion de la ventana agregarGasto
    """

    window = loop()

    window.close()


def loop():
    #Decodifica los datos del json en una estructura de datos 
    data = decode_json()

    #Usuarios_json sera una lista de diccionarios, cada uno representa un gasto
    usuarios_json = data['usuarios']

    window = build(usuarios_json)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()


        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break


        if ((event == '-agregar-') and (values['-usuario-'] != '')):
            
            


            #Crea un diccionario gasto para almacenar los datos del gasto, recibido en los elementos de la pantalla
            usuario = {
                'nombre' : values['-usuario-'],
                'monto' :  values['-monto-']
                #el codigo unico de cada usuario asignado como el tamaño actual de la lista de usuario mas uno
                #'codigo': str(len(usuarios_json) + 1)
            }

            #Agrega el dicc a la lista de diccionarios 
            usuarios_json.append(usuario)

            
            #Sobreescribe el json con la nueva lista
            write_json(data)

            window['-lista_usuarios-'].update([[usuarios_json[row][keys] for keys in usuarios_json[row].keys()]for row in range(len(usuarios_json))]
)


        
    return window