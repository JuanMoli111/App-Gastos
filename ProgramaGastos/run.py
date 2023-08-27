
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


    La idea es empezar a salvar los datos desde agosto como marcados por tipo de gasto

    Luego para las compras de las que tenga datos mas especificos Se incluy en el analisis por producto

    Asi podemos tener x ejemplo dos compras de tipo supermercado
    pero una sin productos y otra con tres productos

    Asi se puede analizar en general y tambien en particular

    (en ambas podemos hacer analisis por tipos de gasto. aunque para analisis por productos o analisis de datos mas particulares solo contaremos los gastos incluidos en el analisis por productos. esto va a reducir el numero de datos pero vamos a contar con que los que haya son precisos y a la larga será de utilidad igualmente)
    


"""