![grade_management_system](https://github.com/user-attachments/assets/a615d451-7741-4b1a-ad5f-3b534fba951c)

# 📊 Sistema de Gestión de Calificaciones

### 📘 English version  
[Click here to see the README in English](./README_EN.md)

## 📌 Descripción del Proyecto

Este ejercicio forma parte del **Módulo 1 – Semana 2 del entrenamiento** y tiene como objetivo desarrollar un sistema interactivo en Python que permita gestionar calificaciones de estudiantes y analizar estadísticas de rendimiento de manera sencilla y funcional.

---

## 🎯 Funcionalidades

- Validar una calificación individual (de 0 a 100) y determinar si aprueba (≥ 60).
- Ingresar una lista de calificaciones válidas separadas por comas.
- Calcular el promedio de las calificaciones ingresadas.
- Contar cuántas calificaciones son mayores que un valor específico.
- Verificar si una calificación específica se encuentra en la lista y cuántas veces aparece.

---

## 🧠 Lógica Implementada

- Se emplean estructuras condicionales (`if`, `if-else`, `if-elif-else`) para validar y evaluar los datos ingresados.
- Se utilizan ciclos `for` y `while` para recorrer listas, controlar el menú, validar entradas y contar valores.
- Se usan `break` y `continue` para optimizar el control de flujo.
- Cada funcionalidad está dividida en funciones reutilizables para mantener el código limpio y ordenado.

---

## ✅ Validaciones Realizadas

- Verificación de rangos válidos para cada calificación (0-100).
- Manejo de entradas inválidas con `try-except`.
- Exclusión de datos erróneos en listas antes de procesarlas.
- Casos considerados:
  1. Ingreso de valores no numéricos
  2. Calificaciones fuera de rango
  3. Listas vacías
  4. Detección de duplicados
  5. Verificación de presencia de una calificación específica

---

## 📁 Estructura del Código

- Código dividido en funciones para: validación individual, cálculo de promedio, conteo, verificación.
- Menú principal que dirige a cada funcionalidad.
- Comentarios explicativos en cada sección del código.

---

## 🧩 Justificación Técnica

El código está construido de manera modular para favorecer su mantenimiento y expansión:

- `float()` se usó para permitir decimales en las calificaciones.
- Se integraron estructuras de control de flujo que permiten navegación fluida.
- Se priorizó la validación robusta de datos y la retroalimentación clara al usuario.
- La organización del menú y las funciones permite ampliar fácilmente con nuevas funcionalidades.

---

## 🚀 Mejoras Futuras

- Exportar e importar listas de calificaciones desde archivos externos (CSV, JSON).
- Agregar funcionalidades para modificar o eliminar calificaciones.
- Implementar una interfaz gráfica con Tkinter o PyQt.
- Incluir gráficos estadísticos de desempeño usando `matplotlib`.

---

## 💻 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado (versión recomendada: 3.8 o superior).
2. Clona este repositorio desde GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Grade-management-system.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd Grade-management-system
   ```

4. Ejecuta el archivo principal:

   ```bash
   python grade_management_system.py
   ```

5. Explora las opciones del menú para validar, calcular y analizar calificaciones.

---
