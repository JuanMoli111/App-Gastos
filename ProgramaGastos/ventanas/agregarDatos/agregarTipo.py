import PySimpleGUI as sg



#Recibimos por parametro la lista de tipos de gasto

def build(tipos):
    """
    build de la ventana para agregar tipos, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """

    layout = [

        [sg.Text("Ingrese un tipo de gasto")],
        [sg.Input(key='-tipo-', pad = (4,4))], [sg.Button("Agregar",key = '-agregar-')],

        [sg.Text("Tipos")],
        [sg.Table(values = tipos, justification="center", headings = ['Tipos'], auto_size_columns=False, col_widths=[32, 32],row_height=15, pad=(5, 5), key = '-lista_tipos-')],

        [sg.Button('aceptar'),sg.Button('salir')]



    ]
    
    ##Retorna un objeto Window que crea pasandole el layout creado
    return sg.Window(title = "Agregar Tipo", layout = layout, margins = (100,100))
