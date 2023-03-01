import PySimpleGUI as sg

from funciones import *

def start():

    """
        lanza la ejecucion de la ventana agregarGasto
    """

    window = loop()

    window.close()



def loop():

    ##Decodificar data, necesito los users y los tipos
    data = decode_json()

    #Pasarle los users y los tipos al window BUILD
    lista_usuarios = data['usuarios']
    lista_tipos = data['tipos']
    lista_gastos = data['gastos']
    
    lista_productos = []



    window = build(lista_usuarios, lista_tipos, lista_productos)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        if event == "test":
            print(values['-date-'])
            #testIt(lista_gastos)
                    
        if event == "-disable_gastos-":
            
            #DONE
            print(window['-tipo_gasto-'].update(disabled=False))

            print(values['-tipo_gasto-'])

            #window['-tipo_gastos-'].update(values['-disable_gastos-'])
            window['-tipo_gasto-'].update(disabled=values['-disable_gastos-'])


        if event == "-disable_productos-":
            disable_productos = not disable_productos
            window['-disable_productos-'].update(disable_productos)


        if event == "-agregar_producto-":

            ##analizar el tema del peso / cantidad (El user deberia poder seleccionar si el producto se cuenta en peso o cantidades, por ejemplo frutas o harina se mide en peso, mientras que por ej esponjas o trapos se miden en cantidades) (no estaria mal que el usuario tambien defina si el peso se midio en kilos o litros)
            producto = {
                'monto' : values['-monto-'],
                'peso'  : values['-peso-'],
                'tipo'  : values['-tipo-'],
            }

            lista_productos.append(producto)

            

            #values['-lista_productos-'] = lista_productos
            values['-monto-'] = 0
            window['-lista_productos-'].update(list(map(lambda prod: prod['tipo'], lista_productos)))

        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        if event == "aceptar":

   

            ##Calcula el monto total con la lista de productos
            monto_total = sum(map(lambda prod : float(prod["monto"]),lista_productos))
           
            #Crea un diccionario gasto para almacenar los datos del gasto, recibido en los elementos de la pantalla
            gasto = {
                ##monto deberia ser la suma de los montos en la lista de productos
                'monto_total' : monto_total,
                'fecha' : values['-date-'],
                'lista_productos': lista_productos,
                'comprador': values['-autor-'][0],

                #el codigo unico de cada gasto asignado como el tamaño actual de la lista de gastos mas uno
                'codigo': str(len(lista_gastos) + 1)

            }

            #Agrega el dicc a la lista de diccionarios 
            lista_gastos.append(gasto)
            
            #Sobreescribe el json con la nueva lista
                
            print("comprador fue " + gasto['comprador'])

            #ACTUALIZAR EL MONTO DEL USUARIO QUE COMPRO
            for i in range(len(lista_usuarios)):

                ##Si encuentra el user con el nombre que realizó el gasto
                if(lista_usuarios[i]['nombre'] == gasto['comprador']):

                    ##Resta al monto el total del gasto 
                    lista_usuarios[i]['monto'] = float(lista_usuarios[i]['monto']) - monto_total
                    break
            


            ##Actualiza el usuario
            data['usuarios'] = lista_usuarios

            #Sobreescribe el json con la nueva lista
            write_json(data)

 
            ##Resetea la lista de productos
            lista_productos=[]
            window['-lista_productos-'].update(lista_productos)


    return window


##  -------------------
##  BUILD DE LA VENTANA
#NOTA  diseñar mejor la disposicion de los elementos , dividiendo para que sea intuitivo
# #los datos del gasto de los productos que añade a la lista de productos del gasto
    
#Recibimos por parametro la lista de usuarios y de tipos de gasto, 
def build(lista_usuarios, lista_tipos, lista_productos, disable_productos = False):
    """
    build de la ventana para agregar gastos, esta funcion crea el layout de la ventana,
    este es una lista de elementos de PysimpleGUI,
     y lo usa para generar la ventana luego retorna la ventana
    """

    lista_usuarios = list(map(lambda u: u['nombre'], lista_usuarios))
    
    layout= [[sg.Text('Agregar gasto', size=(30,1), font=("Sawasdee", 25), justification= 'center')],

            #INGRESAR DATOS DEL GASTO, RESPECTIVAMENTE MONTO DIA MES AÑO PESO EN KG O ML TIPO DE COMPRA Y USUARIO QUE LA REALIZO
            
            #Elemento calendario, Seteamos las abreviaciones y los nombres de los meses en ESPAÑOL
            [sg.Push()],
            [sg.CalendarButton(button_text='Seleccionar fecha', size=(20, 1), key='-date-',format="%d-%m-%Y" ,day_abbreviations=["DO","LU","MA","MI","JU","VI","SA"],month_names=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])],
            
            [sg.Checkbox('Incluir en el analisis por gasto', key='-disable_gastos-',enable_events=True)],
            [sg.Text('Tipo de Gasto'), sg.Input(key='-tipo_gasto-')],


            [sg.Checkbox('Incluir en el analisis por productos', key='-disable_productos-')],
            #AGREGAR PRODUCTOS A LA LISTA DE PRODUCTOS DEL GASTO
            [sg.Push(), sg.Text('Producto'), sg.InputCombo(lista_tipos, size=(20, len(lista_tipos) if len(lista_tipos) <= 10 else 10), key = '-tipo-', disabled=disable_productos)],
            [sg.Push(), sg.Text('Monto'),   sg.Input(key='-monto-', disabled=disable_productos)],  
            
            [sg.Radio('Peso', 'loss', size=(12, 1)), sg.Radio('Cantidad', 'loss', default=True, size=(12, 1))],

            [sg.Push(), sg.Text('Peso'),    sg.Input(key='-peso-', disabled=disable_productos)],   
            
            ## Aceptar (agregar gasto y guardar) --- Boton para salir 
            [sg.Push(), sg.Button('Agregar producto',key='-agregar_producto-'),sg.Listbox(lista_productos,key='-lista_productos-',size=(20,5))],

            [sg.Push(), sg.Text('Seleccione quien realizo la compra')],
            [sg.Push(), sg.Listbox(lista_usuarios, size= (20,len(lista_usuarios) if len(lista_usuarios) <= 10 else 10), key = '-autor-', enable_events = True)],
            

            ## Aceptar (agregar gasto y guardar) --- Boton para salir 
            [sg.Button('aceptar'),sg.Button('salir'),sg.Button('test')]
            
            ]

    return sg.Window(title = "Agregar Gasto", layout = layout, margins = (100,100),resizable=True,auto_size_buttons=True,auto_size_text=True, element_justification='center', no_titlebar=True,disable_close=False, disable_minimize=False, alpha_channel=1, grab_anywhere=True)




def testIt(lista_gastos):
    monto = 0
