import PySimpleGUI as sg


conv = ['Nico','Diego','Juan']

tipos = ['Leche','Arroz']


def build():
    """
    build de la ventana para agregar gastos, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """


    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado

    layout= [[sg.Text('Agregar gasto', size=(30,1), font=("Sawasdee", 25), justification= 'center')],

            [sg.Text('Monto'),sg.Input(key='-monto-')],   
            [[sg.Text('Dia'),sg.Input(key='-dia-')],[sg.Text('Mes'),sg.Input(key='-mes-')],[sg.Text('Año'),sg.Input(key='-anio-')]],   
            [sg.Text('Tipo de gasto'),sg.Input(key='-tipo-')],          

            [sg.Text('Seleccione el autor de la compra')],

            [sg.InputCombo(tipos, size=(20, 2))],      

            [sg.Listbox(conv, size= (20,len(conv)), key = '-autor-', enable_events = True)],
            [sg.Button('aceptar'),sg.Button('salir')]

            ]   


    return sg.Window(title = "Hello World", layout = layout, margins = (100,100))
