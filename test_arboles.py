from arbol import *
from arbol_binario import *

# --- Ejemplo de uso de Árbol General ---
print("--- Árbol General ---")

# Nodo raíz
raiz_general = crear_nodo_arbol("A")

# Nodos hijos de la raíz
b = crear_nodo_arbol("B")
c = crear_nodo_arbol("C")
d = crear_nodo_arbol("D")

agregar_hijo(raiz_general, b)
agregar_hijo(raiz_general, c)
agregar_hijo(raiz_general, d)

# Nodos hijos de 'B'
e = crear_nodo_arbol("E")
f = crear_nodo_arbol("F")
agregar_hijo(b, e)
agregar_hijo(b, f)

# Nodos hijos de 'C'
g = crear_nodo_arbol("G")
agregar_hijo(c, g)

# Nodos hijos de 'E'
h = crear_nodo_arbol("H")
i = crear_nodo_arbol("I")
agregar_hijo(e, h)
agregar_hijo(e, i)


print("Árbol completo (estructura de lista):", raiz_general)

print("\nRecorrido (Árbol General):")
recorrer(raiz_general)
print()

print(f"\nAltura del Árbol General: {altura(raiz_general)}")

# --- Ejemplo de uso de Árbol Binario ---
print("\n\n--- Árbol Binario ---")

# Nodo raíz
raiz_binario = crear_nodo_arbol_binario("A")

# Nodos hijos de la raíz
b = crear_nodo_arbol_binario("B")
c = crear_nodo_arbol_binario("C")
set_hijo_izquierdo(raiz_binario, b)
set_hijo_derecho(raiz_binario, c)

# Nodos hijos de 'B'
d = crear_nodo_arbol_binario("D")
e = crear_nodo_arbol_binario("E")
set_hijo_izquierdo(b, d)
set_hijo_derecho(b, e)

# Nodos hijos de 'C'
f = crear_nodo_arbol_binario("F")
g = crear_nodo_arbol_binario("G")
set_hijo_izquierdo(c, f)
set_hijo_derecho(c, g)

# Nodos hijos de 'E'
h = crear_nodo_arbol_binario("H")
set_hijo_izquierdo(e, h)

print("Árbol binario completo (estructura de lista):", raiz_binario)

print("\nRecorrido Preorden (Árbol Binario):")
recorrer_preorden_binario(raiz_binario)
print()

print("\nRecorrido Inorden (Árbol Binario):")
recorrer_inorden_binario(raiz_binario)
print()

print("\nRecorrido Postorden (Árbol Binario):")
recorrer_postorden_binario(raiz_binario)
print()

print(f"\nAltura del Árbol Binario: {altura_binario(raiz_binario)}")