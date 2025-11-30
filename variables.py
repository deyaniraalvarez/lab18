# variables.py

def declarar_variables():
    nombre = input("Ingrese nombre: ")
    entero = int(input("Ingrese un entero: "))
    flotante = float(input("Ingrese un número decimal (ej: 3.14): "))
    booleano_str = input("Ingrese True o False: ")
    booleano = booleano_str.strip().lower() in ("true", "1", "sí", "si")

    print('\n-- Variables ingresadas --')
    print(f"Nombre: {nombre}")
    print(f"Entero: {entero}")
    print(f"Flotante: {flotante}")
    print(f"Booleano: {booleano}")

    return nombre, entero, flotante, booleano
    