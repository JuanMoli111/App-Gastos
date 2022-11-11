import PySimpleGUI as sg




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

        [sg.Button("NOne")]



    ]

    return sg.Window(title = "Agregar Tipo", layout = layout)
