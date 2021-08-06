import PySimpleGUI as sg


def build():
    """
    build de la ventana para agregar datos, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """


    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Necesitamos tres botones para cada tipo de dato a agregar

    layout = [

        [sg.Button('Agregar gastos', key = '-gasto-')],
        [sg.Button('Agregar tipos de producto', key = '-tipo-')],
        [sg.Button('Agregar convivientes', key = '-conv-')]

    ]

    return sg.Window('Datos').Layout(layout)
