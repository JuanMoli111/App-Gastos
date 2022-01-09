import PySimpleGUI as sg


#Deberiamos recibir por parametro la lista de convivientes y de tipos de gasto, 
#Lista por defecto...
#conv = ['Usuario']
#tipos = ['Productos','Servicios']


def build(usuarios = ['Usuario'], tipos = ['Productos','Seios']):
    """
    build de la ventana para agregar gastos, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """


    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado

    layout= [[sg.Text('Agregar gasto', size=(30,1), font=("Sawasdee", 25), justification= 'center')],

            [sg.Text('Monto'),sg.Input(key='-monto-', pad = (4,4))],   

            [[sg.Text('Dia'),sg.Input(key='-dia-', pad = (4,4))],[sg.Text('Mes'),sg.Input(key='-mes-', pad = (4,4))],[sg.Text('Año'),sg.Input(key='-anio-', pad = (4,4))]],   

            [sg.Text('Seleccione el tipo de la compra')],
            
            [sg.InputCombo(tipos, size=(20, 2), key = '-tipo-')],

            [sg.Text('Seleccione quien realizo la compra')],
            [sg.Listbox(usuarios, size= (20,len(usuarios) if len(usuarios) <= 10 else 10), key = '-autor-', enable_events = True)],


            [sg.Button('aceptar'),sg.Button('salir')]

            ]   


    return sg.Window(title = "Agregar Gasto", layout = layout, margins = (100,100))
