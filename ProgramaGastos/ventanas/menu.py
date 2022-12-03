import PySimpleGUI as sg


def build():
    """
    Loop de la ventana de menú inicio que capta los eventos al apretar las opciones
    """

    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado
    layout= [[sg.Text("PROGRAMA DE GESTION DE GASTOS", size=(40,4), font=("Sawasdee", 15), justification= 'center')],

                [sg.Button('Agregar Datos',key = '-agregar-')],
                [sg.Button('Visualizar los datos',key = '-visualizar-')],
                [sg.Button('Eliminar datos',key = '-eliminar-')],

                [sg.Button('Salir', key = 'salir')]
                
            ]   
            
    
    return sg.Window('Menu principal').Layout(layout)