def calcular_promedio(lista,valor):
    """
    recibe una lista de numeros y un numero valor y calcula el promedio de la lista y dice si el promedio es mayor a valor
    debe retornar: true si es mayor y false si no lo es
    """
    suma= sum(lista)
    promedio = suma / len (lista)
    return promedio > valor

entrada = [10,20,30,40]
valor=24
resultado= calcular_promedio(entrada,valor)

