from funciones import decode_json

import PySimpleGUI as sg



def start():

    """
    Lanza la ejecución de la primer ventana
    """
    window = loop()

    window.close()

def loop():

    #Decodifica el json para recuperar la informacion (Si decodifico el JSON en el loop event, y lo envia a la ventana, sería esta la forma de actualziar la informacion mientras se introduce?)
    data = decode_json()

    lista_gastos = data["gastos"]
    lista_usuarios = data["usuarios"]
    lista_tipos = data["tipos"]

    window = build(lista_gastos,lista_usuarios,lista_tipos)

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break



    return window



#BUILD DE LA VENTANA

#Recibir del componente una lista de gastos generada decodificando el json que registra los gastos
#Usar la lista para visualizar los datos en el layout de la ventana
def build(lista_gastos,lista_usuarios,lista_tipos):

    #Generar una lista de los gastos, que pueda usarse en la tabla de visualizacion de los datos
    data_gastos = [[lista_gastos[row][keys] for keys in lista_gastos[row].keys()]for row in range(len(lista_gastos))]
    data_usuarios = [[lista_usuarios[row][keys] for keys in lista_usuarios[row].keys()]for row in range(len(lista_usuarios))]
    data_tipos = [lista_tipos[row] for row in range(len(lista_tipos))]


    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado
    layout= [[sg.Text("ELIMINACION DE DATOS", size=(40,2), font=("Sawasdee", 15), justification= 'center')],

                ##TENEMOS QUE MANDAR A ELIMINAR EL DATO QUE FUE SELECCIONADO DE ALGUNA DE LAS TRES TABLAS, AL MOMENTO DE DAR A ELIMINAR

                #Tabla con todos los gastos 
                [sg.Table(values = data_gastos, justification="center", headings=['Monto ', 'Fecha ', 'Peso ', 'Autor', 'Tipo'], auto_size_columns=False, col_widths=[20, 20],row_height=18, pad=(2, 2))],
                            
                #Tabla de users
                [sg.Table(values = data_usuarios, justification="center", headings=['Nombre ', 'Monto '], auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(4, 4))],
                
                #Tabla con los tipos de gastos
                [sg.Table(values = data_tipos, justification="center", headings=['Tipo'], auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(6, 6))],

                
                [sg.Button('eliminar')], [sg.Button('salir')]
            ]   
            

    return sg.Window(title = "Eliminacion de datos", layout = layout, margins = (100,100))