import PySimpleGUI as sg

from funciones import *

from datetime import datetime

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

            #Los productos no pueden agregarse vacios o con campos incompletos
            if(values['-tipo-']) == '':
                sg.popup("Olvido ingresar el tipo de producto")
            elif(values['-precio_producto-']) == '':
                sg.popup("Olvido ingresar el precio del producto")
            else:
                producto = {
                    'precio' : values['-precio_producto-'],
                    'peso'  : values['-peso-'],
                    'tipo'  : values['-tipo-']
                }

                lista_productos.append(producto)

                #Resetear la lista de productos, el precio y el peso
                window['-precio_producto-'].update('')
                window['-peso-'].update('')
                window['-lista_productos-'].update(list(map(lambda prod: prod['tipo'], lista_productos)))

        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        elif event == "aceptar":

            cancelar_operaciones = False

            #Deberia hacer una funcion que haga las comprobaciones

            ##Si algun campo está vacio debe mostrar un popup al respecto y no dejar guardar el producto, y no hacer operaciones innecesarias
            if(values['-tipo_gasto-']) == '':
                sg.popup("Olvido ingresar el tipo de gasto")
            elif(values['-precio-']) == '':
                sg.popup("Olvido ingresar el precio del gasto")
            elif(values['-autor-'].__len__() == 0):
                sg.popup("Olvido ingresar el autor del gasto")
            else:

                #Si esta activado el analisis por productos debe verificar que los precios de los productos coincidan con el total del gasto, si no coinciden debe activar el booleano CANCELAR_OPERACIONES
                #Si esta desactivado el analisis por productos entonces solo debe setear el monto del precio del gasto
                if(values['-disable_productos-']):
                    total_precios_productos = sum(map(lambda prod : float(prod["precio"].replace(",",".")),lista_productos))
                                            
                    #Si los precios no coinciden mostrar un popup y cancelar todo el resto de las operaciones
                    if(total_precios_productos != float(values['-precio-'].replace(",","."))):
                        sg.popup("Error la suma de los montos de los productos no coinciden con el total del gasto")
                        cancelar_operaciones = True
                    else:
                        monto_total = total_precios_productos
                else:
                    monto_total = float(values['-precio-'].replace(",","."))

                if(not(cancelar_operaciones)):


                        autor = values['-autor-'][0]

                        #Buscamos al usuario autor de la compra para salvarlo
                        condicion = lambda x: x == autor
                        usuario = next((x for x in lista_usuarios if condicion(x['nombre'])), None)
                        
                        #Salvamos la lista de gastos del usuario
                        lista_gastos = usuario['gastos']

                        #Si el usuario olvido poner la fecha pone la fecha del dia, sino deja la que asigno el usuario
                        fecha = datetime.now().strftime('%d-%m-%Y') if values['-date-'] == '' else values['-date-']
                        
                        
                        #Crea un diccionario gasto para almacenar los datos del gasto, recibido en los elementos de la pantalla
                        gasto = {

                            'monto_total' : monto_total,
                            'tipo_gasto' : values['-tipo_gasto-'],
                            'fecha' : fecha,

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

                        sg.popup("El gasto se agrego exitosamente")

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


