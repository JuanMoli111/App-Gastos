import PySimpleGUI as sg

from funciones import *

from ventanas.AgregarDatos.agregarUsuario import build


def start():

    """
        lanza la ejecucion de la ventana agregarGasto
    """

    window = loop()

    window.close()


def loop():
    #Decodifica los datos del json en una estructura de datos 
    data = decode_json()

    #lista_usuarios sera una lista de diccionarios, cada dicc representa un usuario
    lista_usuarios = data['usuarios']

    window = build(lista_usuarios)


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
                #'codigo': str(len(lista_usuarios) + 1)
            }

            #Agrega el dicc a la lista de diccionarios 
            lista_usuarios.append(usuario)

            
            #Sobreescribe el json con la nueva lista
            write_json(data)

            #Podria hacer el update en todo momento pero lo hago luego de clickear el boton agregar
            window['-lista_usuarios-'].update([[lista_usuarios[row][keys] for keys in lista_usuarios[row].keys()]for row in range(len(lista_usuarios))]
)


        
    return window