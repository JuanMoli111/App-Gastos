import PySimpleGUI as sg

lista_tipos = ['Coca-cola', 'CocaCola', 'Type3', 'Type4', 'Type5']

layout = [
    [sg.Text('Select Type:')],
    [sg.Input(key='-tipo-', enable_events=True), sg.Listbox(values=lista_tipos, size=(20, 5), key='-list_tipo-', enable_events=True)],
    [sg.Button('OK'), sg.Button('Exit')]
]

window = sg.Window('Listbox Example', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-list_tipo-':
        # When an item in the listbox is clicked, update the input field
        selected_item = values['-list_tipo-'][0]
        window['-tipo-'].update(value=selected_item)
    elif event == '-tipo-':
        typed_value = values['-tipo-'].strip().lower()
        # Update the listbox with filtered items
        filtered_types = [t for t in lista_tipos if typed_value in t.lower()]
        window['-list_tipo-'].update(values=filtered_types)

window.close()



    """layout1= [[sg.Text('Agregar gasto', size=(30,1), font=("Sawasdee", 25), justification= 'center')],
            [
            [

            #Elemento calendario, Seteamos las abreviaciones y los nombres de los meses en ESPAÑOL
            [sg.CalendarButton(button_text='Seleccionar fecha', size=(20, 1), key='-date-',format="%d-%m-%Y" ,day_abbreviations=["DO","LU","MA","MI","JU","VI","SA"],month_names=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])],
                        
            [sg.Text('Tipo de Gasto',justification='left')], 
            [sg.Input(key='-tipo_gasto-',justification='left')],
            [sg.Text('Precio',justification='left')], 
            [sg.Input(key='-precio-',justification='left')],

            [sg.Text('Seleccione quien realizo la compra')],
            [sg.Listbox(lista_usuarios, size= (20,len(lista_usuarios) if len(lista_usuarios) <= 10 else 10), key = '-autor-',enable_events = True)],
            

            [sg.Text('Local')],
            [sg.Listbox(list(map(lambda local: [local['nombre'],local['codigo']], lista_locales)), size= (20,len(lista_locales) if len(lista_locales) <= 10 else 10), key = '-lista_locales-',enable_events = True)],
            [sg.Table(list(map(lambda local: [local['nombre'],local['codigo']], lista_locales)), key = '-tabla_locales-',col_widths=(10,10) ,max_col_width=200,enable_events = True)],
            
            [sg.Button('Agregar local',key='-crear_local-')],
            ],

            [
            #Switch para activar o desactivar el análisis por productos.
            [sg.Push(), sg.Checkbox('Incluir en el analisis por productos', key='-disable_productos-', enable_events=True, default=True)],

            #AGREGAR PRODUCTOS A LA LISTA DE PRODUCTOS DEL GASTO
            [sg.Push(), sg.Text('Producto'), sg.InputCombo(lista_tipos, size=(20, len(lista_tipos) if len(lista_tipos) <= 10 else 10), key = '-tipo-')],

            ##El producto se puede medir en cantidades, o en pesos. El peso debería poder medirse en kilos o en litros
            [[sg.Push(), sg.Radio('Peso', 'loss', size=(10, 1),key='-radio_peso-'), sg.Radio('Cantidad', 'loss', default=True, size=(10, 1),key='-radio_cantidad-')],
            
            [sg.Push(), sg.Text('Peso'), sg.Input(key='-peso-',size=(30,40))]],   
            [sg.Push(), sg.Text('Precio') , sg.Input(key='-precio_producto-',size=(30,40))],
            [sg.Push(), sg.Text('Marca') , sg.Input(key='-marca_producto-',size=(30,40))],
            
            ## Aceptar (agregar producto a la lista) 
    
            [sg.Button('Agregar producto',key='-agregar_producto-'), sg.Text("Total: "), sg.Text('0',key='-monto_total-')],
            [sg.Listbox(lista_productos,key='-lista_productos-',size=(20,5))],
            
            ]],

            ## Aceptar (agregar gasto y guardar) --- Boton para salir 
            [sg.Button('aceptar'),sg.Button('salir')]
            
            ]"""