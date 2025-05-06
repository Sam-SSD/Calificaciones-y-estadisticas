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
- Contar cuántas calificaciones son mayores que un valor específico **y mostrarlas**.
- Verificar si una calificación específica se encuentra en la lista y cuántas veces aparece.
- **Borrar todas las calificaciones ingresadas.**

---

## 🧠 Lógica Implementada

- Se emplea la estructura `match-case` (disponible desde Python 3.10) para organizar de forma clara el flujo del menú principal.
- Se utilizan ciclos `while` para validar entradas y controlar el flujo de ingreso de datos.
- Se aplican comprensiones de listas para filtrar y analizar datos de forma eficiente.
- Cada funcionalidad está separada en funciones específicas, reutilizables y documentadas.
- El sistema responde de forma interactiva con retroalimentación clara para el usuario.

---

## ✅ Validaciones Realizadas

- Verificación de rangos válidos para cada calificación (0-100).
- Manejo de entradas inválidas con `try-except`.
- Exclusión de datos erróneos en listas antes de procesarlas.
- Casos considerados:
  1. Ingreso de valores no numéricos
  2. Calificaciones fuera de rango
  3. Listas vacías
  4. Verificación de presencia de una calificación específica

---

## 📁 Estructura del Código

- Código dividido en funciones para: validación individual, cálculo de promedio, obtención de calificaciones mayores, verificación, ingreso y limpieza de datos.
- El menú principal está implementado con `match-case` para una navegación clara y eficiente.
- Comentarios explicativos en cada función y bloque de lógica.

---

## 🧩 Justificación Técnica

El código está construido de manera modular para favorecer su mantenimiento y expansión:

- `float()` se usó para permitir decimales en las calificaciones.
- Se priorizó la validación robusta de datos y una experiencia interactiva clara.
- El uso de estructuras modernas como `match-case` mejora la legibilidad del menú.
- La organización por funciones permite escalar fácilmente con nuevas funcionalidades.

---

## 🚀 Mejoras Futuras

- Exportar e importar listas de calificaciones desde archivos externos (CSV, JSON).
- Agregar funcionalidades para modificar o eliminar calificaciones específicas.
- Implementar una interfaz gráfica con Tkinter o PyQt.
- Incluir gráficos estadísticos de desempeño usando `matplotlib`.

---

## 💻 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado (versión recomendada: 3.8 o superior).
2. Clona este repositorio desde GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Grade-Management-System.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd Grade-Management-System
   ```

4. Ejecuta el archivo principal:

   ```bash
   python grade_management_system.py
   ```

5. Explora las opciones del menú para validar, calcular y analizar calificaciones.

---
