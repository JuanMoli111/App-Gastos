import PySimpleGUI as sg



def build(lista_usuarios):
    """
    build de la ventana para agregar usuarios, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """
    #Generar una lista de los usuarios, que pueda usarse en la tabla de visualizacion de los datos
    data_usuarios = [[lista_usuarios[row][keys] for keys in lista_usuarios[row].keys()]for row in range(len(lista_usuarios))]

   

    layout = [

        [sg.Text("Ingrese un usuario nuevo")],
        [sg.Text("Nombre: ") , sg.Input(key='-usuario-', pad = (4,4))],
        [sg.Text("Monto: ") , sg.Input(key='-monto-', pad = (4,4)) ],
        [sg.Button("Agregar",key = '-agregar-')],

        
        [sg.Text("Usuarios")],
        [sg.Table(values = data_usuarios, justification="center",headings = ['Nombre','Monto'], auto_size_columns=False, col_widths=[16, 16],  row_height=18, pad=(4, 4), key = '-lista_usuarios-')], 

        [sg.Button('aceptar'),sg.Button('salir')]

        
    ]

    return sg.Window(title = "Agregar Usuario", layout = layout, margins = (100,100))