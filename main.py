# Sistema de validación de calificaciones

# Función para validar que la calificación esté entre 0 y 100
def validar_calificacion(calificacion):
    while True:
        try:
            calificacion = float(input(calificacion))
            if calificacion < 0 or calificacion > 100:
                print("Por favor, ingrese una calificación entre 0 y 100.")
            else:
                if calificacion >= 60:
                    print("El estudiante ha aprobado.")
                else:
                    print("El estudiante ha reprobado.")
                return calificacion
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


print("----------Bienvenido al sistema de gestión de calificaciones----------")

# Calificación de una nota
calificacion = validar_calificacion("Ingrese una calificación numérica (0-100): ")

# Calcular el promedio
while True:
    try:
        lista_calificaciones = input("Ingrese las calificaciones separadas por comas (ejemplo: 70,80,90): ")
        lista_calificaciones = [float(x) for x in lista_calificaciones.split(",")]
        if len(lista_calificaciones) == 0:
            print("La lista de calificaciones no puede estar vacía.")
        else:
            promedio = calcular_promedio(lista_calificaciones)
            print(f"El promedio de las calificaciones es: {promedio:.2f}")
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números válidos separados por comas.")

# Contar calificaciones mayores
while True:
    try:
        valor = float(input("Ingrese un valor para contar cuántas calificaciones son mayores: "))
        contador = contar_mayores(lista_calificaciones, valor)
        print(f"Hay {contador} calificaciones mayores que {valor}.")
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

print("--------------------------------------------------------------------")


