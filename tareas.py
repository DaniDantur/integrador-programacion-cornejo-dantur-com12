from arbol import *

tareas = crear_nodo_arbol('Tareas')
tarea_seleccionada = tareas
ruta_tareas = [tareas]
estado = 'menu'

def agregar_tarea(titulo, descripcion=None):
    tarea = {
        'titulo': titulo,
        'descripcion': descripcion,
        'completada': False,
    }
    return agregar_hijo(tarea_seleccionada, crear_nodo_arbol(tarea))

def mostrar_ruta():
    for i, n in enumerate(ruta_tareas):
        if obtener_valor(n) == 'Tareas':
            print('Tareas', end='')
        else:
            print(f' / {obtener_valor(n)["titulo"]}', end='')
    print('\n')

def mostrar_tareas(nodo):
    if nodo is None:
        return

    mostrar_ruta()

    if obtener_valor(nodo) != 'Tareas':
        valor = obtener_valor(nodo)
        print(f'{'[x]' if valor['completada'] else '[ ]'} {valor['titulo']}')
        if 'descripcion' in valor and valor['descripcion']:
            print('\nDescripción:')
            print(f' {valor["descripcion"]}\n')
    
    for indice, hijo in enumerate(obtener_hijos(nodo)):
        valor = obtener_valor(hijo)
        print(f'{indice + 1}. {'[x]' if valor['completada'] else '[ ]'} {valor['titulo']}', end=' ')
        if not es_hoja(hijo):
            subtareas = len(obtener_hijos(hijo))
            print(f'({'1 subtarea' if subtareas == 1 else f'{subtareas} subtareas'})')
        else:
            print()


def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpiar_pantalla()

    mostrar_tareas(tarea_seleccionada)
    print()

    print(f'{'-' * 40}')
    if estado == 'menu':
        print('a. Agregar tarea')
        if tarea_seleccionada != tareas:
            print('d. Agregar descripción a tarea')
            print('v. Volver atrás')
            print('c. Completar tarea')
            print('b. Borrar tarea')
            print('r. Volver a la raíz')
        print('x. Salir')
        print('Seleccione una tarea ingresando su número:')

        estado = input('> ').strip().lower()
    else:
        opcion = estado

        if opcion == 'a':
            titulo = input('Ingrese el título de la tarea: ')
            agregar_tarea(titulo)

        elif opcion == 'd':
            if tarea_seleccionada != tareas:
                descripcion = input('Ingrese la descripción de la tarea: ')
                valor_tarea = obtener_valor(tarea_seleccionada)
                valor_tarea['descripcion'] = descripcion    

        elif opcion == 'v':
            if len(ruta_tareas) > 1:
                ruta_tareas.pop()
                tarea_seleccionada = ruta_tareas[-1]

        elif opcion == 'c':
            if tarea_seleccionada != tareas:
                valor_tarea = obtener_valor(tarea_seleccionada)
                valor_tarea['completada'] = True
                print(f'Tarea "{valor_tarea["titulo"]}" marcada como completada.')

        elif opcion == 'b':
            if tarea_seleccionada != tareas:
                valor_tarea = obtener_valor(tarea_seleccionada)
                confirmar = input(f'¿Está seguro de que desea eliminar la tarea "{valor_tarea["titulo"]}"? (s/n): ').strip().lower()
                if confirmar == 's':
                    ruta_tareas.pop()
                    eliminar_hijo(ruta_tareas[-1], tarea_seleccionada)
                    if len(ruta_tareas) > 0:
                        tarea_seleccionada = ruta_tareas[-1]
                    else:
                        tarea_seleccionada = tareas

        elif opcion == 'r':
            tarea_seleccionada = tareas
            ruta_tareas = [tareas]
        
        elif opcion == 'x':
            confirmar = input('¿Está seguro de que desea salir? (s/n): ').strip().lower()
            if confirmar == 's':
                limpiar_pantalla()
                break
        
        elif opcion.isnumeric() and int(opcion) > 0:
            pos = int(opcion) - 1

            if pos < 0 or pos >= len(obtener_hijos(tarea_seleccionada)):
                print('Número de tarea no válido.')
                continue
            
            tarea_seleccionada = obtener_hijos(tarea_seleccionada)[pos]
            ruta_tareas.append(tarea_seleccionada)
            valor_tarea = obtener_valor(tarea_seleccionada)
        
        estado = 'menu'


