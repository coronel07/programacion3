def ordenamiento_fusion(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izquierda = ordenamiento_fusion(lista[:mid])
    derecha = ordenamiento_fusion(lista[mid:])
    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
