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


#BUILD DE LA VENTANA

#Recibimos por parametro la lista de tipos de gasto

def build(lista_tipos):
    """
    build de la ventana para agregar tipos, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """

    layout = [

        [sg.Text("Ingrese un tipo de gasto")],
        [sg.Input(key='-tipo-', pad = (4,4))], [sg.Button("Agregar",key = '-agregar-')],

        [sg.Text("Tipos")],
        [sg.Table(values = lista_tipos, justification="center", headings = ['Tipos'], auto_size_columns=False, col_widths=[32, 32],row_height=15, pad=(5, 5), key = '-lista_tipos-')],

        [sg.Button('aceptar'),sg.Button('salir')]


    ]
    
    
    ##Retorna un objeto Window que crea pasandole el layout creado
    return sg.Window(title = "Agregar Tipo", layout = layout, margins = (100,100),resizable=True,auto_size_buttons=True,auto_size_text=True, element_justification='center', no_titlebar=True,disable_close=False, disable_minimize=False, alpha_channel=1, grab_anywhere=True)