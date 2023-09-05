from funciones import decode_json

import PySimpleGUI as sg


def start():

    """
    Lanza la ejecución de la primer ventana
    """
    window = loop()

    window.close()

def loop():

    #Decodifica el json para recuperar la informacion
    data = decode_json()


    lista_usuarios = data["usuarios"]


    window = build(lista_usuarios)

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()


        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break


        if event == '-usuario-':

            #Salvamos el nombre del usuario seleccionado para analisis de datos
            usuario_seleccionado = values['-usuario-'][0]

            #Buscamos al usuario en la lista epara salvar sus datos
            usuario = next((x for x in lista_usuarios if x['nombre'] == usuario_seleccionado), None)

            lista_gastos = usuario['gastos']

            #Convierte la lista de gastos, que es una lista de diccionarios-gasto, en una lista de listas-gasto, que es el formato necesario para la tabla
            lista_formateada = [[lista_gastos[row][keys] for keys in lista_gastos[row].keys()]for row in range(len(lista_gastos))]
 
            #Actualiza la tabla de gastos
            window['-tabla_gastos-'].update(lista_formateada)
        
    return window


##BUILD DE LA VENTANA

#Recibir del componente una lista de gastos generada decodificando el json que registra los gastos
#Usar la lista para visualizar los datos en el layout de la ventana
def build(lista_usuarios):

    nombres_usuarios = list(map(lambda usuario: usuario["nombre"], lista_usuarios))


    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado
    layout= [[sg.Text("VISUALIZACION DE GASTOS", size=(40,2), font=("Sawasdee", 15), justification= 'center')],

                #Selecciona un usuario para visualizar sus gastos
                [sg.Text("Seleccione el usuario"), sg.Listbox(nombres_usuarios, size=(10, len(nombres_usuarios) if len(nombres_usuarios) <= 5 else 5), key = '-usuario-', enable_events=True)],

                #Tabla con los gastos
                [sg.Table(values = [], headings=['Monto Total','Tipo De Gasto','Fecha','Codigo','Lista Productos','Lalalala','Lalalala','Lalalala'],key = '-tabla_gastos-', justification='center', auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(2, 2))],

    
                [sg.Button('Salir', key = 'salir')]
            ]   
            

    return sg.Window(title = "Visualizacion de gastos",layout = layout,  margins=(100,100), element_padding=(20,20), element_justification='center', no_titlebar=True, grab_anywhere=True)
