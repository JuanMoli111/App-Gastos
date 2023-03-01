
import sys
sys.path.append(R'C:\Users\EXO\AppData\Local\Programs\Python\Python38\Lib\site-packages')

from ventanas.menu import start;


if __name__ == "__main__":
    start()


"""
    -Crear una opcion para setear si un gasto debe ser contabilizado en el registro?
    -Crear una opcion para setear si un gasto debe ser contabilizado en el analisis de datos de productos?

    -Crear el "Tipo de gasto" Asi un gasto de 5 productos en el supermercado será de Tipo "supermercado".
     De esta manera puede analizar por tipos de gasto, ya que el analisis por productos a veces resulta incompleto por falta de precios tickets cantidades etc.


     ##Para esto podría haber ticks que habiliten cada posible dato a ingresar.
     Por ejemplo un gasto tendria un tipo de gasto y un monto. (Asi tamb diferenciaria los ingresos q no tendrian listas de prod)

    Luego tendría un tick para agregar lista de productos. Lo cual solo debería hacer si tengo todos los precios y pesos/cantidades de los prod
        Para cada prod podria tener un swithc para setear por kilos, o por cantidad. por ejemplo un maple de huevo se mide en cantidad en vez de kilos


"""