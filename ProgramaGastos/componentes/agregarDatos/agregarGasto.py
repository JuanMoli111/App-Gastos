import PySimpleGUI as sg

from ventanas.agregarDatos.agregarGasto import build

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

    #Usuarios_json sera una lista de diccionarios, cada uno representa un gasto
    #usuarios_json = data['usuarios']
    #tipos_json = data['tipos']
    lista_productos = []
    #Pasarle los users y los tipos al window BUILD

    usuarios_json = data['usuarios']


    window = build(usuarios_json,data['tipos'],lista_productos)

    

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        
        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        if event == "-agregar_producto-":

            ##analizar el tema del peso / cantidad (El user deberia poder seleccionar si el producto se cuenta en peso o cantidades, por ejemplo frutas o harina se mide en peso, mientras que huevos o sahumerios se miden en cantidades) (no estaria mal que el usuario tambien defina si el peso se midio en kilos o litros)
            producto = {
                'monto' : values['-monto-'],
                'peso'  : values['-peso-'],
                'tipo'  : values['-tipo-'],
            }

            lista_productos.append(producto)

            values['-lista_productos-'] = lista_productos
            values['-monto-'] = 0

        #Al aceptar, el gasto deberia tener una lista PRODUCTOS, estos Con un MONTO y el TIPO DE GASTO Y PESO/CANTIDAD
        #Osea que deberia haber un boton para agregar PRODUCTOS al gasto con su propio TIPO MONTO Y PESO/CANTIDAD


        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        if event == "aceptar":

            gastos_json = data['gastos']

            ##Calcula el monto total con la lista de productos
            monto_total = sum(map(lambda prod : int(prod["monto"]),lista_productos))
           
            #Crea un diccionario gasto para almacenar los datos del gasto, recibido en los elementos de la pantalla
            gasto = {
                ##monto deberia ser la suma de los montos en la lista de productos
                'monto_total' : monto_total,
                'fecha' : [values['-dia-'] + '/' + values['-mes-'] + '/' + values['-anio-']],
                'lista_productos': lista_productos,
                'comprador': values['-autor-'][0],

                #el codigo unico de cada gasto asignado como el tamaño actual de la lista de gastos mas uno
                'codigo': str(len(gastos_json) + 1)

            }

            #Agrega el dicc a la lista de diccionarios 
            gastos_json.append(gasto)
            
            #Sobreescribe el json con la nueva lista
                
            print("comprador fue " + gasto['comprador'])

            #ACTUALIZAR EL MONTO DEL USUARIO QUE COMPRO
            for i in range(len(usuarios_json)):
                print(f"user en {i}" + str(usuarios_json[i]))
                if(usuarios_json[i]['nombre'] == gasto['comprador']):
                    print(f"user en {i} monto" + str(usuarios_json[i]['monto']))

                    usuarios_json[i]['monto'] = float(usuarios_json[i]['monto']) - monto_total

                    break
            
            data['usuarios'] = usuarios_json

            #Sobreescribe el json con la nueva lista
            write_json(data)

            #write_json(usuarios_json)
            #ACTUALIZAR EL MONTO DEL USUARIO QUE COMPRO
            #autor = find(lambda aut : aut['nombre'] == gasto['comprador'],usuarios_json)
            #autor["monto"] -= monto_total


            ##Resetea la lista de productos
            lista_productos=[]


    return window
