import PySimpleGUI as sg



def build(usuarios):
    """
    build de la ventana para agregar usuario, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """

    layout = [

        [sg.Text("Ingrese un usuario nuevo")],
        [sg.Input(key='-usuario-', pad = (4,4)), sg.Button("Agregar",key = '-agregar-')],

        [sg.Text("Usuarios")],
        [sg.Table(values = usuarios, justification="center",headings = ['user'], auto_size_columns=False, col_widths=[16, 16],row_height=10, pad=(2, 2), key = '-lista_usuarios-')],

        [sg.Button('aceptar'),sg.Button('salir')]

        
    ]

    return sg.Window(title = "Agregar Gasto", layout = layout, margins = (100,100))
