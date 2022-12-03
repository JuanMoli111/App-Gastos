import PySimpleGUI as sg


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