def crear_nodo_arbol(valor):
    return [valor]

def agregar_hijo(nodo_padre, nodo_hijo):
    nodo_padre.append(nodo_hijo)

def obtener_valor(nodo):
    return nodo[0]

def obtener_hijos(nodo):
    return nodo[1:] 

def es_hoja(nodo):
    return len(obtener_hijos(nodo)) == 0

def recorrer(nodo):
    if nodo is None:
        return

    print(obtener_valor(nodo), end=" ")
    for hijo in obtener_hijos(nodo):
        recorrer(hijo)

def altura(nodo):
    if nodo is None:
        return -1
    elif not nodo or es_hoja(nodo):
        return 0
    
    max_altura_hijos = 0
    for hijo in obtener_hijos(nodo):
        max_altura_hijos = max(max_altura_hijos, altura(hijo))
    return 1 + max_altura_hijos
