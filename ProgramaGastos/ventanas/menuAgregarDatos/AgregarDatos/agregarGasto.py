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
    
    ###eliminar luego de hacer el test
    lista_tipos = data['tipos']
    #lista_gastos = data['gastos']

    #La lista de productos se inicializa vacia
    lista_productos = []

    window = build(lista_usuarios, lista_tipos, lista_productos)


    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()


        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break
        

        ##Si desactiva el análisis por producto, la ventana debe inhabilitar el ingreso de datos de lista de producots, precios y cantidades.
        elif event == "-disable_productos-":

            
            #Vaciar los campos llenados que se van a bloquear
            if(not values['-disable_productos-']):
                window['-peso-'].update('')
                window['-lista_productos-'].update('')


            #Update elementos, habilitandolos o deshabilitandolos
            window['-peso-'].update(            disabled= not values['-disable_productos-'])
            window['-radio_peso-'].update(      disabled= not values['-disable_productos-'])
            window['-radio_cantidad-'].update(  disabled= not values['-disable_productos-'])
            window['-tipo-'].update(            disabled= not values['-disable_productos-'])
            window['-precio_producto-'].update( disabled= not values['-disable_productos-'])
            
            window['-agregar_producto-'].update(disabled= not values['-disable_productos-'])
            window['-lista_productos-'].update( disabled=not values['-disable_productos-'])


        #Agregar producto a la lista de productos del gasto 
        elif event == "-agregar_producto-":

            producto = {
                'precio' : values['-precio_producto-'],
                'peso'  : values['-peso-'],
                'tipo'  : values['-tipo-'],
            }

            lista_productos.append(producto)

            #Resetear la lista de productos, el precio y el peso
            window['-precio_producto-'].update('')
            window['-peso-'].update('')
            window['-lista_productos-'].update(list(map(lambda prod: prod['tipo'], lista_productos)))

        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        elif event == "aceptar":


            
            #print("TIPO DE MONTO TOTAL LINE106: " + str(type(sum(map(lambda prod : float(prod["precio"]),lista_productos)))))

            autor = values['-autor-'][0]

            #Buscamos al usuario autor de la compra para salvarlo
            condition = lambda x: x == autor
            usuario = next((x for x in lista_usuarios if condition(x['nombre'])), None)
            
            #Salvamos la lista de gastos del usuario
            lista_gastos = usuario['gastos']


            #FIX: fecha debe setearse por defecto 
            #FIX: los productos no pueden agregarse vacios o con campos incompletos
            #FIX: el precio total debe coincidir con el total de los precios por productos si es que se incluyo el analisis por producto. 

            #FIX: en esta funcion, si el analisis por productos está habilitado debe verificar que la suma de los precios de los prod coincida con el gasto total, y si no esta habilitado debe considerar solo el precio del gasto

            #---Los errores en el ingreso de datos pueden informarse con un pop up. Tambien debería informar el ingreso exitoso del gasto

            if(not values['-disable_productos-']):
                monto_total = float(values['-precio-'].replace(",","."))
            else:
                ##Calcula el monto total con la lista de productos
                monto_total = sum(map(lambda prod : float(prod["precio"].replace(",",".")),lista_productos))
            
            print(values['-disable_productos-'])


            #Crea un diccionario gasto para almacenar los datos del gasto, recibido en los elementos de la pantalla
            #(Si el gasto debe ser registrado para analisis)
            gasto = {

                'monto_total' : monto_total,
                'tipo_gasto' : values['-tipo_gasto-'],
                'fecha' : values['-date-'],

                #el codigo unico de cada gasto asignado como el tamaño actual de la lista de gastos mas uno
                'codigo': str(len(lista_gastos) + 1)

            }

            ##Si esta activado el analisis por producto, salvar la lista de productos en el gasto.
            if (values['-disable_productos-']): gasto['lista_productos'] = lista_productos
               
            
            #Agrega el gasto (dicc) a la lista de gastos (dicc)
            lista_gastos.append(gasto)
                            
            #ACTUALIZAR EL MONTO DEL USUARIO QUE COMPRO
            usuario['monto'] -= monto_total

            #Sobreescribe el json con la nueva lista de users
            write_json(data)

 
            ##Resetea la lista de productos
            lista_productos=[]
            window['-lista_productos-'].update(lista_productos)


    return window



##  -------------------         #NOTA  diseñar mejor la disposicion de los elementos: quiero que la fecha, tipo de gasto, precio y lista de usuarios este justificado a la izquierda
##  BUILD DE LA VENTANA         ###   todo lo relativo a analisis por producto justificado a la derecha,  Y los botones para agregar gasto y para salir queden debajo

#Recibimos por parametro la lista de usuarios y de tipos de gasto, 
def build(lista_usuarios, lista_tipos, lista_productos):
    """
    build de la ventana para agregar gastos, esta funcion crea el layout de la ventana,
    este es una lista de elementos de PysimpleGUI,
     y lo usa para generar la ventana luego retorna la ventana
    """

    lista_usuarios = list(map(lambda u: u['nombre'], lista_usuarios))
    

    layout= [[sg.Text('Agregar gasto', size=(30,1), font=("Sawasdee", 25), justification= 'center')],

            #INGRESAR DATOS DEL GASTO, RESPECTIVAMENTE MONTO TOTAL, FECHA, TIPO DE GASTO, USUARIO QUE LO REALIZO ,LISTA DE PRODUCTOS, QUE INCLUYE: PRECIO , PESO O CANTIDAD Y TIPO DE PRODUCTO 
            #Elemento calendario, Seteamos las abreviaciones y los nombres de los meses en ESPAÑOL
            [sg.CalendarButton(button_text='Seleccionar fecha', size=(20, 1), key='-date-',format="%d-%m-%Y" ,day_abbreviations=["DO","LU","MA","MI","JU","VI","SA"],month_names=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])],
                        
            [sg.Text('Tipo de Gasto',justification='left')], 
            [sg.Input(key='-tipo_gasto-')],
            [sg.Text('Precio',justification='left')], 
            [sg.Input(key='-precio-')],

            [sg.Text('Seleccione quien realizo la compra')],
            [sg.Listbox(lista_usuarios, size= (20,len(lista_usuarios) if len(lista_usuarios) <= 10 else 10), key = '-autor-', enable_events = True)],
            

            #Switch para activar o desactivar el análisis por productos.
            [sg.Push(), sg.Checkbox('Incluir en el analisis por productos', key='-disable_productos-', enable_events=True, default=True)],

            #AGREGAR PRODUCTOS A LA LISTA DE PRODUCTOS DEL GASTO
            [sg.Push(), sg.Text('Producto'), sg.InputCombo(lista_tipos, size=(20, len(lista_tipos) if len(lista_tipos) <= 10 else 10), key = '-tipo-')],

            ##El producto se puede medir en cantidades, o en pesos. El peso debería poder medirse en kilos o en litros
            [[sg.Push(), sg.Radio('Peso', 'loss', size=(10, 1),key='-radio_peso-'), sg.Radio('Cantidad', 'loss', default=True, size=(10, 1),key='-radio_cantidad-')],
            
            [sg.Push(), sg.Text('Peso'), sg.Input(key='-peso-',size=(30,40))]],   
            [sg.Push(), sg.Text('Precio') , sg.Input(key='-precio_producto-',size=(30,40))],

            ## Aceptar (agregar producto a la lista) 
            [sg.Push(), sg.Button('Agregar producto',key='-agregar_producto-'),
             sg.Listbox(lista_productos,key='-lista_productos-',size=(20,5))],


            ## Aceptar (agregar gasto y guardar) --- Boton para salir 
            [sg.Button('aceptar'),sg.Button('salir')]
            
            ]

    return sg.Window(title = "Agregar Gasto", layout = layout, margins = (100,100),resizable=True,auto_size_buttons=True,auto_size_text=True, element_justification='center', no_titlebar=True,disable_close=False, disable_minimize=False, alpha_channel=1, grab_anywhere=True)


