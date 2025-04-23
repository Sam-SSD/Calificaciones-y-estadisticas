# Sistema de validación de calificaciones

# Función para validar que la calificación esté entre 0 y 100
def validar_calificacion(calificacion):
    while True:
        try:
            calificacion = float(input(calificacion))
            if 0 <= calificacion <= 100:
                print(f"Calificación válida: {calificacion}")
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

# Función para calcular el promedio de una lista de calificaciones
def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    return promedio


# Función para contar cuántas calificaciones son mayores que un valor específico, teniendo en cuenta que no tengo una lista de calificaciones
def contar_mayores(calificaciones, valor):
    contador = 0
    for calificacion in calificaciones:
        if calificacion > valor:
            contador += 1
    return contador

def verificar_calificacion(calificaciones, calificacion):
    contador = 0
    for c in calificaciones:
        if c == calificacion:
            contador += 1
            print(f"La calificación {calificacion} se encuentra en la lista.")
            break
    else:
        print(f"La calificación {calificacion} no se encuentra en la lista.")
    return contador

#hacer un menu de opciones

def menu():
    print("\n1. Validar calificación individual")
    print("2. Ingresar calificaciones")
    print("3. Calcular promedio de calificaciones")
    print("4. Contar calificaciones mayores")
    print("5. Verificar calificación en lista")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Bucle principal del menú

print("----------Bienvenido al sistema de gestión de calificaciones----------")
lista_calificaciones = []
while True:
    opcion = menu()
    if opcion == "1": # Validar una calificación individual,
        calificacion = validar_calificacion("Ingrese una calificación numérica (0-100) Aprueba con 60: ")

    elif opcion == "2": # Ingresar calificaciones (separadas por comas) (0-100)
        while True:
            try:
                lista_calificaciones = input("Ingrese las calificaciones separadas por comas (0-100) (ejemplo: 70,80,90): ")
                lista_calificaciones = [float(x) for x in lista_calificaciones.split(",")]
                lista_calificaciones = [x for x in lista_calificaciones if 0 <= x <= 100]
                if len(lista_calificaciones) == 0:
                    print("No se han ingresado calificaciones válidas. Por favor, intente nuevamente.")
                else:
                    print(f"Calificaciones ingresadas: {lista_calificaciones}")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos separados por comas.")

    elif opcion == "3": # Calcular promedio de las calificaciones
        if len(lista_calificaciones) == 0:
            print("No se han ingresado calificaciones. Por favor, primero ingrese calificaciones.")
        else:
            promedio = calcular_promedio(lista_calificaciones)
            print(f"El promedio de las calificaciones es: {promedio:.2f}")

    elif opcion == "4": # Contar calificaciones mayores que un valor
        if len(lista_calificaciones) == 0:
            print("No se han ingresado calificaciones. Por favor, primero ingrese calificaciones.")
        else:
            while True:
                try:
                    valor = float(input("Ingrese un valor para contar cuántas calificaciones son mayores: "))
                    contador = contar_mayores(lista_calificaciones, valor)
                    print(f"Hay {contador} calificaciones mayores que {valor}.")
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

    elif opcion == "5": # Verificar si una calificación está en la lista
        if len(lista_calificaciones) == 0:
            print("No se han ingresado calificaciones. Por favor, primero ingrese calificaciones.")
        else:
            while True:
                try:
                    calificacion = float(input("Ingrese la calificación a verificar: "))
                    contador = verificar_calificacion(lista_calificaciones, calificacion)
                    print(f"La calificación {calificacion} aparece {contador} veces en la lista.")
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

print("--------------------------------------------------------------------")
