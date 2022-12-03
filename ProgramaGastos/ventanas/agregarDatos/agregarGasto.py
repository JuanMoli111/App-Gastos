import PySimpleGUI as sg


#Recibimos por parametro la lista de usuarios y de tipos de gasto, 

def build(lista_usuarios, lista_tipos, lista_productos):
    """
    build de la ventana para agregar gastos, esta funcion crea el layout
     y lo usa para generar la ventana luego retorna la ventana
    """
#NOTA  diseñar mejor la disposicion de los elementos , dividiendo para que sea intuitivo
# #los datos del gasto de los productos que añade a la lista de productos del gasto
    
    lista_usuarios = list(map(lambda u: u['nombre'], lista_usuarios))

    #Crea el layout de la ventana, este es una lista de elementos de PysimpleGUI
    #Agregamos los elementos necesarios para recibir la informacion del gasto desde teclado
    layout= [[sg.Text('Agregar gasto', size=(30,1), font=("Sawasdee", 25), justification= 'center')],

            #INGRESAR DATOS DEL GASTO, RESPECTIVAMENTE MONTO DIA MES AÑO PESO EN KG O ML TIPO DE COMPRA Y USUARIO QUE LA REALIZO
            [[sg.Text('Dia'),sg.Input(key='-dia-', pad = (4,4))],[sg.Text('Mes'),sg.Input(key='-mes-', pad = (4,4))],[sg.Text('Año'),sg.Input(key='-anio-', pad = (4,4))]],   

            #AGREGAR PRODUCTOS A LA LISTA DE PRODUCTOS DEL GASTO
            [sg.Text('Seleccione el tipo de la compra')],
            [sg.InputCombo(lista_tipos, size=(20, len(lista_tipos) if len(lista_tipos) <= 10 else 10), key = '-tipo-')],
            [sg.Text('Monto'),sg.Input(key='-monto-', pad = (4,4))],   
            [sg.Text('Peso'),sg.Input(key='-peso-', pad = (4,4))],   
            
            ## Aceptar (agregar gasto y guardar) --- Boton para salir 
            [sg.Button('Agregar producto',key='-agregar_producto-'),sg.Listbox(lista_productos,key='-lista_productos-',size=(20,5))],

            [sg.Text('Seleccione quien realizo la compra')],
            [sg.Listbox(lista_usuarios, size= (20,len(lista_usuarios) if len(lista_usuarios) <= 10 else 10), key = '-autor-', enable_events = True)],


            ## Aceptar (agregar gasto y guardar) --- Boton para salir 
            [sg.Button('aceptar'),sg.Button('salir')]

            ]   


    return sg.Window(title = "Agregar Gasto", layout = layout, margins = (100,100))