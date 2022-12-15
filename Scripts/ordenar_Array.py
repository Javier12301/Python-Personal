#Ordenar array
#Menor a mayor
def ordenar_menor_a_mayor(array):
    if len(array) <= 1:
        return array
    
    inicio = array[0]
    izquierda = []
    derecha = []

    for i in range(1, len(array)):
                izquierda.append(array[i]) if array[i] < inicio else derecha.append(array[i])
    return ordenar_menor_a_mayor(izquierda) + [inicio] + ordenar_menor_a_mayor(derecha) 

def ordenar_mayor_a_menor(array):
    if len(array) <= 1:
        return array
    
    inicio = array[0]
    izquierda = []
    derecha = []

    for i in range(1, len(array)):
                izquierda.append(array[i]) if array[i] > inicio else derecha.append(array[i])
    return ordenar_mayor_a_menor(izquierda) + [inicio] + ordenar_mayor_a_menor(derecha) 





lista = [21,5,9,23,46,10, 28, 21]

lista_ordenada = ordenar_menor_a_mayor(lista)
print(lista_ordenada)
