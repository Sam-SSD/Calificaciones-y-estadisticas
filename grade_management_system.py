# Sistema de validación de calificaciones

# Función para ingresar múltiples calificaciones
# Solicita una cadena de texto con números separados por comas, los convierte a float,
# y filtra solo los que estén entre 0 y 100. Devuelve la lista válida.
def ingresar_calificaciones():
    while True:
        entrada = input("Ingrese calificaciones separadas por comas (0-100): ")
        try:
            # Convertimos cada valor separado por coma a float, eliminando espacios
            calificaciones = [float(x.strip()) for x in entrada.split(",")]
            # Solo se conservan las calificaciones válidas dentro del rango
            calificaciones_validas = [c for c in calificaciones if 0 <= c <= 100]
            if not calificaciones_validas:
                print("No se ingresaron calificaciones válidas.")
            else:
                print(f"Calificaciones registradas: {calificaciones_validas}")
                return calificaciones_validas
        except ValueError:
            print("Entrada no válida. Use solo números separados por comas.")


# Función para validar una única calificación numérica
# Verifica si está entre 0 y 100 e indica si aprueba (>= 60) o no
def validar_calificacion(mensaje):
    while True:
        try:
            calificacion = float(input(mensaje))
            if 0 <= calificacion <= 100:
                # Operador ternario para mostrar el estado de aprobación
                estado = "aprueba" if calificacion >= 60 else "no aprueba"
                print(f"La calificación {calificacion} es válida y {estado}.")
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entre 0 y 100.")


# Función para calcular el promedio de una lista de calificaciones
# Retorna 0 si la lista está vacía
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0


# Función que obtiene todas las calificaciones mayores a un valor dado
# Devuelve una lista con esas calificaciones
def obtener_mayores(calificaciones, valor):
    return [c for c in calificaciones if c > valor]


# Función para verificar si una calificación específica aparece en la lista
# Imprime cuántas veces aparece y retorna ese número
def verificar_calificacion(calificaciones, calificacion):
    veces = calificaciones.count(calificacion)
    if veces > 0:
        print(f"La calificación {calificacion} se encuentra {veces} vez/veces en la lista.")
    else:
        print(f"La calificación {calificacion} no se encuentra en la lista.")
    return veces


# Función para mostrar el menú de opciones y retornar la elección del usuario
def menu():
    print("\n-------------------------------------------------------")
    print("1. Validar calificación individual")
    print("2. Ingresar calificaciones")
    print("3. Calcular promedio de calificaciones")
    print("4. Contar calificaciones mayores a un valor")
    print("5. Verificar calificación en lista")
    print("6. Borrar todas las calificaciones")
    print("7. Salir")
    print("-------------------------------------------------------")
    return input("Seleccione una opción: ").strip()


# --------------------------- PROGRAMA PRINCIPAL ---------------------------

print("---------- Bienvenido al sistema de gestión de calificaciones ----------")
lista_calificaciones = []  # Lista principal donde se almacenan las calificaciones

# Ciclo principal del programa
while True:
    opcion = menu()  # Se obtiene la opción del usuario

    # Estructura de control match-case (similar a switch-case) para cada opción
    match opcion:
        case "1":  # Validar una sola calificación
            validar_calificacion("Ingrese una calificación (0-100): ")

        case "2":  # Ingresar una nueva lista de calificaciones
            lista_calificaciones = ingresar_calificaciones()

        case "3":  # Calcular el promedio de las calificaciones ingresadas
            if not lista_calificaciones:
                print("Primero debe ingresar calificaciones.")
            else:
                promedio = calcular_promedio(lista_calificaciones)
                print(f"Promedio de calificaciones: {promedio:.2f}")

        case "4":  # Contar y mostrar calificaciones mayores a cierto valor
            if not lista_calificaciones:
                print("Primero debe ingresar calificaciones.")
            else:
                try:
                    valor = float(input("Ingrese el valor de comparación (0-100): "))
                    if 0 <= valor <= 100:
                        mayores = obtener_mayores(lista_calificaciones, valor)
                        cantidad = len(mayores)
                        print(f"\nSe encontraron {cantidad} calificación(es) mayor(es) a {valor}.")
                        if cantidad > 0:
                            print(f"Calificaciones mayores: {mayores}")
                    else:
                        print("El valor debe estar entre 0 y 100.")
                except ValueError:
                    print("Entrada no válida. Ingrese un número válido.")

        case "5":  # Verificar si una calificación específica está en la lista
            if not lista_calificaciones:
                print("Primero debe ingresar calificaciones.")
            else:
                try:
                    calificacion = float(input("Ingrese la calificación a buscar: "))
                    verificar_calificacion(lista_calificaciones, calificacion)
                except ValueError:
                    print("Entrada no válida. Ingrese un número válido.")

        case "6":  # Eliminar todas las calificaciones de la lista
            if not lista_calificaciones:
                print("No hay calificaciones registradas para borrar.")
            else:
                confirmacion = input("¿Está seguro de borrar todas las calificaciones? (s/n): ").strip().lower()
                if confirmacion in ["s", "sí", "si"]:
                    lista_calificaciones.clear()
                    print("Todas las calificaciones han sido eliminadas.")
                else:
                    print("Acción cancelada.")

        case "7":  # Salir del programa
            print("Saliendo del programa. Gracias por usar el sistema.")
            break

        case _:  # Opción inválida
            print("Opción inválida. Por favor, seleccione una opción del 1 al 7.")

print("-----------------------------------------------------------------------")
