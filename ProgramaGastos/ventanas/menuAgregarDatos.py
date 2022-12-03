import PySimpleGUI as sg


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
