def crear_nodo_arbol_binario(valor):
    return [valor, None, None]

def set_hijo_izquierdo(nodo_padre, nodo_hijo):
    nodo_padre[1] = nodo_hijo

def set_hijo_derecho(nodo_padre, nodo_hijo):
    nodo_padre[2] = nodo_hijo

def get_hijo_izquierdo(nodo):
    return nodo[1]

def get_hijo_derecho(nodo):
    return nodo[2]

def obtener_valor(nodo):
    return nodo[0]

def recorrer_preorden_binario(nodo):
    if nodo is None:
        return

    print(obtener_valor(nodo), end=" ")
    recorrer_preorden_binario(get_hijo_izquierdo(nodo))
    recorrer_preorden_binario(get_hijo_derecho(nodo))

def recorrer_inorden_binario(nodo):
    if nodo is None:
        return

    recorrer_inorden_binario(get_hijo_izquierdo(nodo))
    print(obtener_valor(nodo), end=" ")
    recorrer_inorden_binario(get_hijo_derecho(nodo))

def recorrer_postorden_binario(nodo):
    if nodo is None:
        return

    recorrer_postorden_binario(get_hijo_izquierdo(nodo))
    recorrer_postorden_binario(get_hijo_derecho(nodo))
    print(obtener_valor(nodo), end=" ")

def altura_binario(nodo):
    if nodo is None:
        return -1 
    
    altura_izq = altura_binario(get_hijo_izquierdo(nodo))
    altura_der = altura_binario(get_hijo_derecho(nodo))
    
    return 1 + max(altura_izq, altura_der)
