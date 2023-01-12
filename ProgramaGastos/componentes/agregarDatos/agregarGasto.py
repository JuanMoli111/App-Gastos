import PySimpleGUI as sg

from ventanas.AgregarDatos.agregarGasto import build

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

        if event == "-agregar_producto-":

            ##analizar el tema del peso / cantidad (El user deberia poder seleccionar si el producto se cuenta en peso o cantidades, por ejemplo frutas o harina se mide en peso, mientras que por ej esponjas o trapos se miden en cantidades) (no estaria mal que el usuario tambien defina si el peso se midio en kilos o litros)
            producto = {
                'monto' : values['-monto-'],
                'peso'  : values['-peso-'],
                'tipo'  : values['-tipo-'],
            }

            lista_productos.append(producto)

            values['-lista_productos-'] = lista_productos
            values['-monto-'] = 0


        #Si el user clickea aceptar deben guardarse los datos del gasto en un archivo
        if event == "aceptar":

            gastos_json = data['gastos']



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
                'codigo': str(len(gastos_json) + 1)

            }

            #Agrega el dicc a la lista de diccionarios 
            gastos_json.append(gasto)
            
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


    return window
