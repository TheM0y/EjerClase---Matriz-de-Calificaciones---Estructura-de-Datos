import numpy as np

def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número válido.")

NUM_ALUMNOS = pedir_numero("Ingrese el número de alumnos: ")
NUM_MATERIAS = pedir_numero("Ingrese el número de materias: ")

materias = [f"Materia {i+1}" for i in range(NUM_MATERIAS)]
calificaciones = np.random.randint(50, 101, (NUM_ALUMNOS, NUM_MATERIAS))

def mostrar_matriz():
    print("\nMatriz de Calificaciones:")
    encabezado = " " * 10 + "  ".join([f"{materia:^10}" for materia in materias])
    print(encabezado)
    print("-" * len(encabezado))
    
    for i in range(NUM_ALUMNOS):
        fila = f"Alumno {i+1:<3} | " + "  ".join([f"{calificacion:^10}" for calificacion in calificaciones[i]])
        print(fila)

def buscar_calificacion():
    try:
        num_alumno = int(input(f"Ingrese el número de alumno (1 - {NUM_ALUMNOS}): ")) - 1
        num_materia = int(input(f"Ingrese el número de la materia (1 - {NUM_MATERIAS}): ")) - 1

        if 0 <= num_alumno < NUM_ALUMNOS and 0 <= num_materia < NUM_MATERIAS:
            calificacion = calificaciones[num_alumno, num_materia]
            print(f"\nEl alumno {num_alumno + 1} tiene {calificacion} en {materias[num_materia]}.\n")
        else:
            print("Número de alumno o materia fuera de rango.")
    except ValueError:
        print("Error: Ingrese un número válido.")

while True:
    print("\n1. Mostrar matriz de calificaciones")
    print("2. Buscar calificación de un alumno")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_matriz()
    elif opcion == "2":
        buscar_calificacion()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
