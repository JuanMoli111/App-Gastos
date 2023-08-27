import PySimpleGUI as sg

from ventanas.visualizarDatos.visualizarDatos import start as VisualizarDatosStart

from ventanas.menuAgregarDatos.menuAgregarDatos import start as AgregarDatosStart

from ventanas.eliminarDatos.eliminarDatos import start as EliminarDatosStart


sg.theme('Purple')

def start():

    """
    Lanza la ejecución de la primer ventana
    """
    window = loop()

    window.close()

def loop():


    window = build()

    while True:
        ##Lee los eventos y los values de la ventana
        event, values = window.read()

        ##Cierre de la ventana
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir"):
            break

        #Si el user clickea agregar gasto debe dirigir el programa a la ventana de agregar gastos
        if event == "-agregar-":

            window.hide()

            #Moverse a la ventana de agregar gastos
            AgregarDatosStart()

            window.un_hide()

        #Si el user clickea visualizar gasto debe dirigir el programa a la ventana de visualizar gastos
        if event == "-visualizar-":
            
            window.hide()

            #Moverse a la ventana de visualizar gastos
            VisualizarDatosStart()

            window.un_hide()
             
        #Si el user clickea eliminar gasto debe dirigir el programa a la ventana de eliminar gastos
        
        if event == "-eliminar-":
            
            window.hide()

            #Moverse a la ventana de eliminar gastos
            EliminarDatosStart()

            window.un_hide()       
                        
            

    return window


##BUILD DE LA VENTANA

def build():

    layout = [
        
        
                [sg.Text("PROGRAMA DE GESTION DE GASTOS" , font=("Sawasdee", 15), justification= 'center', text_color='blue')],

                [sg.Button('Agregar Datos',key = '-agregar-', size=(16,2), pad=(10,10)),
                sg.Button('Visualizar los datos',key = '-visualizar-', size=(16,2), pad=(20,20)),
                sg.Button('Eliminar datos',key = '-eliminar-', size=(16,2), pad=(10,10))],

                
                [sg.Button('Salir', key = 'salir')]
                
            ]
            
    return sg.Window('Menu principal', layout, size=(500,400),resizable=True,auto_size_buttons=True,auto_size_text=True, element_padding=(50,60), element_justification='center', no_titlebar=True,disable_close=False, disable_minimize=False, alpha_channel=1, grab_anywhere=True)