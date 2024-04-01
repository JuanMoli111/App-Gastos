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

    lista_usuarios = data['usuarios']
    lista_tipos = data['tipos']
    lista_locales = data['locales']

    lista_marcas = list(set(prod["marca"] for gasto in lista_usuarios[0]["gastos"] for prod in gasto.get("lista_productos", []) if prod.get("marca")))
    lista_tipos = list(set(prod["tipo"] for gasto in lista_usuarios[0]["gastos"] for prod in gasto.get("lista_productos", []) if prod.get("tipo")))


    #La lista de productos se inicializa vacia
    lista_productos = []

    data_selected = []

    #Pasarle los users y los tipos al window BUILD
    window = build(lista_usuarios, lista_tipos, lista_productos, lista_locales, lista_marcas)
    window_agregar_local = None        

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()
 

        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","Salir"):
            break
        

        ##Si desactiva el análisis por producto, la ventana debe inhabilitar el ingreso de datos de lista de producots, precios y cantidades.
        elif event == "-disable_productos-":

            
            #Vaciar los campos llenados que se van a bloquear
            if(not values['-disable_productos-']):
                window['-peso-'].update('')
                window['-lista_productos-'].update('')
                window['-monto_total-'].update('')


            #Update elementos, habilitandolos o deshabilitandolos
            window['-peso-'].update(            disabled= not values['-disable_productos-'])
            window['-radio_peso-'].update(      disabled= not values['-disable_productos-'])
            window['-radio_cantidad-'].update(  disabled= not values['-disable_productos-'])
            window['-tipo-'].update(            disabled= not values['-disable_productos-'])
            window['-precio_producto-'].update( disabled= not values['-disable_productos-'])
            window['-marca-'].update(           disabled= not values['-disable_productos-'])
            window['-agregar_producto-'].update(disabled= not values['-disable_productos-'])
            window['-lista_productos-'].update( disabled=not values['-disable_productos-'])


        #Agregar producto a la lista de productos del gasto 
        elif event == "-agregar_producto-":

            tipo = values['-tipo-']
            precio_producto = values['-precio_producto-']
            peso = values['-peso-']
            marca_producto = values['-marca-']

            if(tipo) == '':
                sg.popup("Olvido ingresar el tipo de producto")
            if(precio_producto) == '':
                sg.popup("Olvido ingresar el precio del producto")
            elif(peso) == '':
                sg.popup("Olvido ingresar el peso del producto")
            elif(marca_producto) == '':
                sg.popup("Olvido ingresar la marca del producto")  
            else:
                
                ###
                ###if(tipo not in lista_tipos and "Y")
                try:
                    #Buscar el monto total del gasto
                    monto_total = window['-monto_total-'].get()

                    #Actualizarlo sumandole el precio del producto (monto_total += precio_producto)
                    window['-monto_total-'].update(ConvertirEnFloatTruncado(monto_total) + ConvertirEnFloatTruncado(precio_producto))
                            
                    #Crea el objeto producto para agregarlo al listado en pantalla
                    producto = {
                        'precio' : precio_producto,
                        'peso'  : peso,
                        'tipo'  : tipo,
                        'marca' : marca_producto
                    }

                    lista_productos.append(producto)

                    #Resetear la lista de productos, el precio y el peso
                    window['-precio_producto-'].update('')
                    window['-peso-'].update('')
                    window['-lista_productos-'].update(list(map(lambda prod: prod['tipo'], lista_productos)))
                except ValueError:
                    sg.Popup("Hubo un error en los datos, asegúrese que el precio está bien escrito")


        elif event == '-lista_locales-':
            fila_seleccionada = values['-lista_locales-'][0]
            local_seleccionado = lista_locales[fila_seleccionada]
            print(fila_seleccionada)
            print([values['-lista_locales-']])
            print(local_seleccionado)

        #Si clickea un item de la lista de productos debe setearse el campo de input con ese producto.
        elif event == '-lista_tipos-':
            # When an item in the listbox is clicked, update the input field
            selected_item = values['-lista_tipos-'][0]
            window['-tipo-'].update(value=selected_item)

        #Si clickea un item de la lista de marcas debe setearse el campo de input con ese marcas.
        elif event == '-lista_marcas-':
            # When an item in the listbox is clicked, update the input field
            selected_item = values['-lista_marcas-'][0]
            window['-marca-'].update(value=selected_item)

        #Si el usuario escribe en el input de tipos, debe funcionar un buscador que mostrará las mejores coincidencias
        #de la busqueda en la lista de tipos
        elif event == '-tipo-':
            typed_value = values['-tipo-'].strip()

            filtered_types = filter_lista(typed_value,lista_tipos,2)
            print(window['-lista_tipos-'])
            window['-lista_tipos-'].update(values=filtered_types)

        #Si el usuario escribe en el input de marcas, debe funcionar un buscador que mostrará las mejores coincidencias
        #de la busqueda en la lista de marcas
        elif event == '-marca-':
            typed_value = values['-marca-'].strip()

            filtered_types = filter_lista(typed_value,lista_marcas,2)

            window['-lista_marcas-'].update(values=filtered_types)
        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        elif event == "Aceptar":

            cancelar_operaciones = False
            

            precio_del_gasto = values['-precio-']

            #
            local = values['-lista_locales-']

            print("Valor al clickear aceptar:" , values['-lista_locales-'])
            #print(data_selected)
            #Deberia hacer una funcion que haga las comprobaciones

            ##Si algun campo está vacio debe mostrar un popup al respecto y no dejar guardar el producto, y no hacer operaciones innecesarias
            if (values['-tipo_gasto-']) == '':
                sg.popup("Olvido ingresar el tipo de gasto")
            elif (precio_del_gasto) == '':
                sg.popup("Olvido ingresar el precio del gasto")
            elif (local == '' or not local):
                sg.popup("Olvido ingresar el local donde realizo la compra")
            elif (values['-autor-'].__len__() == 0):
                sg.popup("Olvido ingresar el autor del gasto")

            else:
                try:



                    #Si esta activado el analisis por productos debe verificar que los precios de los productos coincidan con el total del gasto, si no coinciden debe activar el booleano CANCELAR_OPERACIONES
                    #Si esta desactivado el analisis por productos entonces solo debe setear el monto del precio del gasto
                    if(values['-disable_productos-']):

                        total_precios_productos = ConvertirEnFloatTruncado(sum(map(lambda prod : ConvertirEnFloatTruncado(prod["precio"]),lista_productos)))

                        #Si los precios no coinciden mostrar un popup y cancelar todo el resto de las operaciones
                        if(total_precios_productos != ConvertirEnFloatTruncado(precio_del_gasto)):
                            sg.popup("Error la suma de los montos de los productos no coinciden con el total del gasto")
                            cancelar_operaciones = True
                        else:
                            monto_total = total_precios_productos
                    else:
                        monto_total = ConvertirEnFloatTruncado(precio_del_gasto)


                    if(not(cancelar_operaciones)):


                        autor = values['-autor-'][0]

                        #Buscamos al usuario autor de la compra para salvarlo
                        condicion = lambda x: x == autor
                        usuario = next((x for x in lista_usuarios if condicion(x['nombre'])), None)
                        
                        #Salvamos la lista de gastos del usuario
                        lista_gastos = usuario['gastos']

                        #Si el usuario olvido poner la fecha pone la fecha del dia, sino deja la que asigno el usuario
                        fecha = datetime.now().strftime('%d-%m-%Y') if values['-date-'] == '' else values['-date-']
                        
                        
                        codigo_local = str(int(local[0])+1)
                        print("Codigo local: ", codigo_local)

                        #Crea un diccionario gasto para almacenar los datos del gasto, recibidos en los elementos de la pantalla
                        gasto = {

                            'monto_total' : monto_total,
                            'tipo_gasto' : values['-tipo_gasto-'], 
                            'fecha' : fecha,
                            'codigo_local' : codigo_local,
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


                        window['-monto_total-'].update('0')
                
                        window['-lista_productos-'].update(lista_productos)

                except ValueError:
                    sg.Popup("Hubo un error en los datos, asegúrese que el precio está bien escrito")

        elif event == '-crear_local-' and not window_agregar_local:
            window_agregar_local = crear_ventana_agregar_local()

            while True:
                event, values = window_agregar_local.read()
                
                if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
                    break
                elif event == '-aceptar_agregar_local-':
                    print('que')

                    ##Salva los datos del local crea un diccionario para el local
                    local = {
                        'nombre':     values['-nombre_local-'],
                        'cuit':       values['-cuit_local-'],
                        'direccion':  values['-direccion_local-'],
                        'codigo':     str(len(lista_locales) + 1)
                    }

                    lista_locales.append(local)
                    write_json(data)
                    window['-lista_locales-'].update(list(map(lambda local: [local['nombre'],local['codigo']], lista_locales)))
                    window_agregar_local.close()
                    window_agregar_local = None
                    break
            
        

    return window

def crear_ventana_agregar_local():
    layout = [[sg.Text('Agregar Local')],
 
              [sg.Text('Nombre')],
              [sg.Input(key='-nombre_local-', enable_events=True)],
              [sg.Text('CUIT')],
              [sg.Input(key='-cuit_local-', enable_events=True)],
              [sg.Text('Direccion')],
              [sg.Input(key='-direccion_local-', enable_events=True)],

              [sg.Button('Aceptar',key='-aceptar_agregar_local-'), sg.Button('Exit')]]
              
    return sg.Window('Second Window', layout, finalize=True, modal=True)


##  -------------------         #NOTA  diseñar mejor la disposicion de los elementos: quiero que la fecha, tipo de gasto, precio y lista de usuarios este justificado a la izquierda
##  BUILD DE LA VENTANA         ###   todo lo relativo a analisis por producto justificado a la derecha,  Y los botones para agregar gasto y para salir queden debajo

#Recibimos por parametro la lista de usuarios y de tipos de gasto, 
def build(lista_usuarios, lista_tipos, lista_productos, lista_locales, lista_marcas):
    """
    build de la ventana para agregar gastos, esta funcion crea el layout de la ventana,
    este es una lista de elementos de PysimpleGUI,
     y lo usa para generar la ventana luego retorna la ventana
    """
    #lista_tipos = [gasto for gasto in lista_usuarios[0]['gastos']]

   
    print(lista_tipos)
    print(lista_marcas)
    #print(lista_gastos)

    lista_usuarios = list(map(lambda u: u['nombre'], lista_usuarios))
    lista_locales_formateada = (list(map(lambda local: [local['nombre'], local['codigo']], lista_locales)))

    layout = [
    [sg.Text('Agregar gasto', size=(30, 1), font=("Sawasdee", 25), justification='center')],
    [sg.Column([
        [sg.CalendarButton(button_text='Seleccionar fecha', size=(20, 1), key='-date-', format="%d-%m-%Y", pad=8,
                           day_abbreviations=["DO", "LU", "MA", "MI", "JU", "VI", "SA"],
                           month_names=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                                        "Septiembre", "Octubre", "Noviembre", "Diciembre"])],

        [sg.Text('Tipo de Gasto', justification='left'), sg.Push(),
         sg.Input(key='-tipo_gasto-',size=(20,40), border_width=2, justification='left')],
        [sg.Text('Precio', justification='left'), sg.Push(),
         sg.Input(key='-precio-',size=(20,40), border_width=2, justification='left')],

        [sg.Text('Seleccione quien realizo la compra',pad=10)],
        [sg.Listbox(values=lista_usuarios, size=(20, min(len(lista_usuarios), 10)), key='-autor-', enable_events=True)],

        [sg.Text('Local',pad=10)],
        #[sg.Listbox(values=list(map(lambda local: [local['nombre'], local['codigo']], lista_locales)),
        #            size=(20, min(len(lista_locales), 10)), key='-lista_locales-', enable_events=True),
        [sg.Table(values=lista_locales_formateada, key='-lista_locales-', headings=['Local','Codigo'], size=(30,min(len(lista_locales),10)), auto_size_columns=False, enable_events=True, select_mode=sg.TABLE_SELECT_MODE_BROWSE)],

        [sg.Button('Agregar local', key='-crear_local-',pad=10)]
        ]  , element_justification='center'),
        
        sg.Column([
         
            [sg.Push(), sg.Checkbox('Incluir en el análisis por productos', key='-disable_productos-', enable_events=True, default=True)],

            [sg.Column([
                [sg.Text('Producto')], [sg.Input(key='-tipo-', enable_events=True,size=(22,1))], 
                [sg.Listbox(values=lista_tipos, size=(20, 5), key='-lista_tipos-', enable_events=True)],
            ],element_justification='center'),
            
            sg.Column([
                [sg.Text('Marca')],  [sg.Input(key='-marca-', size=(22, 40))],
            [sg.Listbox(values=lista_marcas, size=(20, 5), key='-lista_marcas-', enable_events=True)],
            ]),],
            
            #sg.InputCombo(values=lista_tipos, size=(20, min(len(lista_tipos), 10)), key='-tipo-')],

            [sg.Text('Peso'),   sg.Input(key='-peso-', size=(11, 40)),sg.Radio('Peso', 'loss', size=(4, 1), key='-radio_peso-'),sg.Radio('Cantidad', 'loss', default=True, size=(10, 1), key='-radio_cantidad-'), sg.Push()],
            [sg.Text('Precio'), sg.Input(key='-precio_producto-', size=(10, 40)),sg.Push()],
            
            [sg.Button('Agregar producto', key='-agregar_producto-',pad=10),
            sg.Listbox(values=lista_productos, key='-lista_productos-', size=(20, 5),pad=10)],

            [sg.Text("Total: "),sg.Text('0', key='-monto_total-',justification='left')]


        ], element_justification='center')],

    [sg.Button('Aceptar',pad=10), sg.Button('Salir',pad=10)],
    
    ]
    
    return sg.Window(title = "Agregar Gasto", layout = layout, margins = (100,100),resizable=True,auto_size_buttons=True,auto_size_text=True, element_justification='center', no_titlebar=True,disable_close=False, disable_minimize=False, alpha_channel=1, grab_anywhere=True)