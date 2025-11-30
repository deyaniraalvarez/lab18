# listas.py

def trabajar_listas():
    print('\n-- Trabajo con Listas --')
    lista = []
    # Añadir 10 elementos de diferentes tipos
    lista.extend([1, 2.5, 'texto', True, None, [1, 2], (3, 4), {'k': 'v'}, 99, 'fin'])
    print('Lista inicial:', lista)

    # Acceder y modificar
    print('Elemento índice 0 antes:', lista[0])
    lista[0] = 42
    print('Después de modificar índice 0:', lista)

    # Agregar un nuevo elemento
    lista.append('nuevo_elemento')
    print('Después de agregar:', lista)

    # Eliminar un elemento (ej: 'fin') si existe
    if 'fin' in lista:
        lista.remove('fin')
        print('Después de eliminar \"fin\":', lista)

    return lista