import PySimpleGUI as sg


def build():
    """
    Loop de la ventana de menú inicio que capta los eventos al apretar las opciones
    """

    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado
    layout= [[sg.Text("PROGRAMA DE GESTION DE GASTOS", size=(30,1), font=("Sawasdee", 25), justification= 'center')],
        
            [sg.Button('Agregar gasto',key = '-agregar-')],
            [sg.Button('salir')]

            ]   
            

    return sg.Window('proyecto').Layout(layout)

