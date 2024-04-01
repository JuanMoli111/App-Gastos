from funciones import decode_json, ConvertirEnFloatTruncado

import matplotlib.pyplot as plt

import PySimpleGUI as sg
import pandas as pd

def create_bar_graph(gasto, tipo_gasto):
    plt.figure(figsize=(16, 8))
    plt.bar(tipo_gasto, gasto)
    plt.title('Gastos por tipo de gasto')
    plt.show()

   
def create_pie_graph(gasto, tipo_gasto):
    plt.figure(figsize=(16, 8))
    plt.pie(tipo_gasto, gasto)
    plt.title('Gastos por tipo de gasto')
    plt.show()


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

    #Dataframe con los gastos del primer usuario
    df = pd.DataFrame(lista_usuarios[0]["gastos"])

    window = build(lista_usuarios)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        print(df)


        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        if event == '-usuario-':

            
            #Salvamos el nombre del usuario seleccionado para analisis de datos
            usuario_seleccionado = values['-usuario-'][0]

            #Buscamos al usuario en la lista para salvar sus datos
            usuario = next((x for x in lista_usuarios if x['nombre'] == usuario_seleccionado), None)

            lista_gastos = usuario['gastos']

            # Generar una lista de los tipos de gasto donde no se repitan
            tipos_de_gasto = list(set(gasto["tipo_gasto"] for gasto in lista_gastos))

            
            #Calcular el monto gastado por tipo de gasto
            montos_totales_por_tipo = [
                sum(gasto["monto_total"] for gasto in lista_gastos if (gasto["tipo_gasto"] == tipo) and gasto["monto_total"]) for tipo in tipos_de_gasto
            ]
            
            create_bar_graph(montos_totales_por_tipo, tipos_de_gasto)
            #create_pie_graph(tipos_de_gasto,montos_totales_por_tipo)


            #Convierte la lista de gastos, que es una lista de diccionarios-gasto, en una lista de listas-gasto, que es el formato necesario para la tabla
            lista_formateada = [[lista_gastos[row][keys] for keys in lista_gastos[row].keys()]for row in range(len(lista_gastos))]
 
            # Obtener una lista de tipos de gasto únicos
            tipos_de_prod = list(set(prod["tipo"] for gasto in lista_gastos for prod in gasto.get("lista_productos", [])))
            
            #Calcular el monto gastado por tipo de producto
            montos_totales_por_tipo_prod = [sum(float(str(prod["precio"]).replace(',', '.')) for gasto in lista_gastos for prod in gasto.get("lista_productos", []) if prod.get("tipo") == tipo) for tipo in tipos_de_prod]
            
            print("TEST:    ",tipos_de_prod)



            tipos_unicos = list(set(palabra for prod in tipos_de_prod for palabra in prod.split('_')))
                        
            print("TEST:    ",tipos_unicos)
            #Calcular el monto gastado por tipo de producto
            montos_totales_por_tipo_prod_unico = [sum(float(str(prod["precio"]).replace(',', '.')) for gasto in lista_gastos for prod in gasto.get("lista_productos", []) if prod.get("tipo") == tipo) for tipo in tipos_unicos]
            
   
            
            #create_bar_graph(montos_totales_por_tipo_prod, tipos_de_prod)


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
    layout= [
                [sg.Text("VISUALIZACION DE GASTOS", size=(40,2), font=("Sawasdee", 15), justification= 'center')],
                [[sg.Text("Seleccione el usuario"), sg.Listbox(nombres_usuarios, size=(10, len(nombres_usuarios) if len(nombres_usuarios) <= 5 else 5), key = '-usuario-', enable_events=True), sg.Text("Desde: "), sg.CalendarButton(button_text='Seleccionar fecha', size=(20, 1), key='-date-',format="%d-%m-%Y" ,day_abbreviations=["DO","LU","MA","MI","JU","VI","SA"],month_names=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]), sg.Text("Hasta: "), sg.CalendarButton(button_text='Seleccionar fecha', size=(20, 1), key='-date-',format="%d-%m-%Y" ,day_abbreviations=["DO","LU","MA","MI","JU","VI","SA"],month_names=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])]],

                [sg.Table(values = [], headings=['Monto Total','Tipo De Gasto','Fecha','Codigo','Lista Productos'],key = '-tabla_gastos-', justification='center', auto_size_columns=False, col_widths=[16, 16],row_height=18, pad=(2, 2)),
                [sg.Text("Analisis de datos"), sg.Button("Barras por tipo",key='-barras-'), sg.Button("Grafico de tarta")]],

                [sg.Button('Salir', key = 'salir')]
            ]   
            

    return sg.Window(title = "Visualizacion de gastos",layout = layout,  margins=(100,100), element_padding=(20,20), element_justification='center', no_titlebar=True, grab_anywhere=True)
