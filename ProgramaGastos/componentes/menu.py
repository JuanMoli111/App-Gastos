import PySimpleGUI as sg

from componentes.visualizarDatos import start as VisualizarDatosStart

from componentes.menuAgregarDatos import start as AgregarDatosStart

from componentes.eliminarDatos import start as EliminarDatosStart

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

    col = [[sg.Button('Salir', key = 'salir',  button_color=('#4287f5'))]]

    layout = [
        
        
                [sg.Text("PROGRAMA DE GESTION DE GASTOS", size=(40,4), font=("Sawasdee", 15), justification= 'center', background_color='#4287f5', text_color='white')],

                [sg.Button('Agregar Datos',key = '-agregar-', button_color=('#4287f5')),
                sg.Button('Visualizar los datos',key = '-visualizar-', button_color=( '#4287f5')),
                sg.Button('Eliminar datos',key = '-eliminar-', button_color=( '#4287f5'))],

                
                [sg.Column(col,justification='right')]
                
            ]   
            
    return sg.Window('Menu principal', layout)
