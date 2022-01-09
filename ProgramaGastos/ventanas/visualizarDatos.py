import PySimpleGUI as sg


#Recibir del componente una lista de gastos generada decodificando el json que registra los gastos
#Usar la lista para visualizar los datos en el layout de la ventana
def build(lista_gastos):

    #Generar una lista de los gastos, que pueda usarse en la tabla de visualizacion de los datos
    data = [[lista_gastos[row][keys] for keys in lista_gastos[row].keys()]for row in range(len(lista_gastos))]


    total = sum([int(lista_gastos[row]['monto']) for row in range(len(lista_gastos))])
    
    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado
    layout= [[sg.Text("VISUALIZACION DE GASTOS", size=(40,2), font=("Sawasdee", 15), justification= 'center')],

                #Tabla con todos los gastos 
                [sg.Table(values = data, justification="center", headings=['Monto ', 'Fecha ', 'Tipo ', 'Autor ',''], auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(2, 2))],
                            

                #Mostrar el total gastado
                [sg.Text(total)],

                #Tabla con el total de gastos de cada user
                [sg.Table(values = data, justification="center", headings=['Monto ', 'Fecha ', 'Tipo ', 'Autor ',''], auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(2, 2))],

                
                [sg.Button('Salir')]
            ]   
            

    return sg.Window('data science').Layout(layout)