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
