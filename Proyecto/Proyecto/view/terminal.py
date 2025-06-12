from model import funciones

def es_entero_entre(valor, minimo, maximo):
    try:
        n = int(valor)
        if n >= minimo and n <= maximo:
            return True
        return False
    except:
        return False

def es_flotante(valor):
    try:
        float(valor)
        return True
    except:
        return False

def mostrar_menu():
    opciones = [
        "e^x",
        "sin(x)",
        "cos(x)",
        "arcsen(x)",
        "arccos(x)",
        "senh(x)",
        "cosh(x)",
        "Salir"
    ]
    while True:
        print("\n" + "="*40)
        print("        CALCULADORA MATEMÁTICA")
        print("="*40)
        for idx, nombre in enumerate(opciones, 1):
            print(" {}. {}".format(idx, nombre))
        print("="*40)

        opcion = input("Selecciona una opción (1-8): ")
        if not es_entero_entre(opcion, 1, 8):
            print("Opción inválida. Por favor, ingresa un número del 1 al 8.")
            continue

        opcion = int(opcion)
        if opcion == 8:
            print("¡Hasta luego!")
            break

        print(f"\n--- Opción seleccionada: {opciones[opcion-1]} ---")
        x = input("Ingresa el valor de x: ")
        if not es_flotante(x):
            print("Por favor, ingresa un número válido para x.")
            continue
        x = float(x)

        if opcion == 1:
            resultado = funciones.exp(x)
        elif opcion == 2:
            resultado = funciones.sin(x)
        elif opcion == 3:
            resultado = funciones.cos(x)
        elif opcion == 4:
            resultado = funciones.arcsin(x)
        elif opcion == 5:
            resultado = funciones.arccos(x)
        elif opcion == 6:
            resultado = funciones.sinh(x)
        elif opcion == 7:
            resultado = funciones.cosh(x)
        else:
            resultado = "Opción no válida."

        print("Resultado: {}".format(resultado))