import PySimpleGUI as sg

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


#BUILD DE LA VENTANA
def build(lista_usuarios):
    """
    build de la ventana para agregar usuarios, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """
    #Generar una lista de los usuarios, que pueda usarse en la tabla de visualizacion de los datos
    data_usuarios = [[lista_usuarios[row][keys] for keys in lista_usuarios[row].keys()]for row in range(len(lista_usuarios))]

   

    layout = [

        [sg.Text("Ingrese un usuario nuevo")],
        [sg.Push(), sg.Text("Nombre: ") , sg.Input(key='-usuario-', pad = (4,4))],
        [sg.Push(), sg.Text("Monto: ") , sg.Input(key='-monto-', pad = (4,4)) ],
        [ sg.Button("Agregar",key = '-agregar-')],

        
        [sg.Text("Usuarios")],
        [sg.Table(values = data_usuarios, justification="center",headings = ['Nombre','Monto'], auto_size_columns=False, col_widths=[16, 16],  row_height=18, pad=(4, 4), key = '-lista_usuarios-')], 

        [sg.Button('aceptar'),sg.Button('salir')]

        
    ]

    return sg.Window(title = "Agregar Usuario", layout = layout, margins = (100,100),resizable=True,auto_size_buttons=True,auto_size_text=True, element_justification='center', no_titlebar=True,disable_close=False, disable_minimize=False, alpha_channel=1, grab_anywhere=True)