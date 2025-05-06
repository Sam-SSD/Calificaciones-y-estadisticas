# Sistema de validación de calificaciones

def validar_calificacion(mensaje):
    while True:
        try:
            calificacion = float(input(mensaje))
            if 0 <= calificacion <= 100:
                estado = "aprueba" if calificacion >= 60 else "no aprueba"
                print(f"La calificación {calificacion} es válida y {estado}.")
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entre 0 y 100.")


def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0


def contar_mayores(calificaciones, valor):
    return sum(1 for c in calificaciones if c > valor)


def verificar_calificacion(calificaciones, calificacion):
    veces = calificaciones.count(calificacion)
    if veces > 0:
        print(f"La calificación {calificacion} se encuentra {veces} vez/veces en la lista.")
    else:
        print(f"La calificación {calificacion} no se encuentra en la lista.")
    return veces


def menu():
    print("\n-------------------------------------------------------")
    print("1. Validar calificación individual")
    print("2. Ingresar calificaciones")
    print("3. Calcular promedio de calificaciones")
    print("4. Contar calificaciones mayores a un valor")
    print("5. Verificar calificación en lista")
    print("6. Salir")
    print("-------------------------------------------------------")
    return input("Seleccione una opción: ").strip()


def ingresar_calificaciones():
    while True:
        entrada = input("Ingrese calificaciones separadas por comas (0-100): ")
        try:
            calificaciones = [float(x.strip()) for x in entrada.split(",")]
            calificaciones_validas = [c for c in calificaciones if 0 <= c <= 100]
            if not calificaciones_validas:
                print("No se ingresaron calificaciones válidas.")
            else:
                print(f"Calificaciones registradas: {calificaciones_validas}")
                return calificaciones_validas
        except ValueError:
            print("Entrada no válida. Use solo números separados por comas.")


# Programa principal
print("---------- Bienvenido al sistema de gestión de calificaciones ----------")
lista_calificaciones = []

while True:
    opcion = menu()

    if opcion == "1":
        validar_calificacion("Ingrese una calificación (0-100): ")

    elif opcion == "2":
        lista_calificaciones = ingresar_calificaciones()

    elif opcion == "3":
        if not lista_calificaciones:
            print("Primero debe ingresar calificaciones.")
        else:
            promedio = calcular_promedio(lista_calificaciones)
            print(f"Promedio de calificaciones: {promedio:.2f}")

    elif opcion == "4":
        if not lista_calificaciones:
            print("Primero debe ingresar calificaciones.")
        else:
            try:
                valor = float(input("Ingrese el valor de comparación (0-100): "))
                if 0 <= valor <= 100:
                    conteo = contar_mayores(lista_calificaciones, valor)
                    print(f"{conteo} calificación(es) mayor(es) a {valor}.")
                else:
                    print("El valor debe estar entre 0 y 100.")
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")

    elif opcion == "5":
        if not lista_calificaciones:
            print("Primero debe ingresar calificaciones.")
        else:
            try:
                calificacion = float(input("Ingrese la calificación a buscar: "))
                verificar_calificacion(lista_calificaciones, calificacion)
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")

    elif opcion == "6":
        print("Saliendo del programa. Gracias por usar el sistema.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")

print("-----------------------------------------------------------------------")
