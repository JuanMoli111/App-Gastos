import PySimpleGUI as sg


#Recibir del componente una lista de gastos generada decodificando el json que registra los gastos
#Usar la lista para visualizar los datos en el layout de la ventana
def build(lista_gastos, lista_usuarios):

    #Generar una lista de los gastos, que pueda usarse en la tabla de visualizacion de los datos
    data_gastos = [[lista_gastos[row][keys] for keys in lista_gastos[row].keys()]for row in range(len(lista_gastos))]
    data_usuarios = [[lista_usuarios[row][keys] for keys in lista_usuarios[row].keys()]for row in range(len(lista_usuarios))]

    #Filtrar los datos de los productos de cada gasto, son innecesarios para calcular los totales xq cada gasto tiene su monto total (total del gasto en todos los productos)
    for dato in data_gastos:
        dato.__delitem__(2)

    monto = sum(map(lambda prod : int(prod["monto_total"]) if int(prod["monto_total"]) > 0 else 0,lista_gastos))

    #Filtramos los INGRESOS para solo sumar los gastos
    lista_gastos_sin_ingresos = list(filter(lambda i: (i['monto_total'] > 0),lista_gastos))

    #Gasto total
    total = sum([int(lista_gastos_sin_ingresos[row]['monto_total']) for row in range(len(lista_gastos_sin_ingresos))])


    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado
    layout= [[sg.Text("VISUALIZACION DE GASTOS", size=(40,2), font=("Sawasdee", 15), justification= 'center')],

                #Tabla con todos los gastos 
                [sg.Table(values = data_gastos, justification="center", headings=['Monto ', 'Fecha ','Autor'], auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(2, 2))],
                            

                #Mostrar el total que tiene 
                [sg.Text(total)],[sg.Text(monto)],

                #debe permitir ver por usuario y por otros criterios

                #Tabla con los usuarios
                [sg.Table(values = data_usuarios, justification="center", headings=['Monto ','Autor'], auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(2, 2))],

                
                [sg.Button('Salir', key = 'salir')]
            ]   
            

    return sg.Window('Visualizacion de datos').Layout(layout)