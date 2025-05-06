![grade_management_system](https://github.com/user-attachments/assets/a615d451-7741-4b1a-ad5f-3b534fba951c)

# 📊 Grade Management System

### 📘 Versión en español  
[Haz clic aquí para ver el README en español](./README.md)

## 📌 Project Description

This exercise is part of **Module 1 – Week 2 of the training program**, and its goal is to build an interactive Python system that helps manage student grades and analyze performance statistics in a simple and functional way.

---

## 🎯 Features

- Validate a single grade (from 0 to 100) and determine if it passes (≥ 60).
- Input a list of valid grades separated by commas.
- Calculate the average of the entered grades.
- Count how many grades are higher than a specific value **and display them**.
- Check whether a specific grade is in the list and how many times it appears.
- **Delete all entered grades.**

---

## 🧠 Implemented Logic

- Uses the `match-case` structure (available since Python 3.10) to organize the main menu flow clearly.
- `while` loops are used to validate user input and control repeated entries.
- List comprehensions are applied to efficiently filter and analyze grade data.
- Each functionality is divided into clean, reusable, and well-documented functions.
- The system responds interactively with clear user feedback.

---

## ✅ Validations Performed

- Range checking to ensure each grade is between 0 and 100.
- Error handling using `try-except` for invalid entries.
- Filtering out invalid data before processing lists.
- Considered scenarios:
  1. Non-numeric input
  2. Out-of-range grades
  3. Empty grade lists
  4. Checking for the presence of a specific grade

---

## 📁 Code Structure

- Functions are used for: individual validation, average calculation, retrieving grades above a value, searching, input, and list clearing.
- The main menu is implemented using `match-case` for clear and efficient navigation.
- Explanatory comments are provided in each section of the code.

---

## 🧩 Technical Justification

The code is built in a modular way to support future scalability and maintenance:

- `float()` is used to allow decimal values in grades.
- Strong validation logic and clear user interaction are prioritized.
- Modern structures like `match-case` improve the menu’s readability.
- The function-based design allows for easy extension with new features.

---

## 🚀 Future Improvements

- Export and import grade lists from external files (CSV, JSON).
- Add functionality to modify or delete specific grades.
- Implement a graphical user interface with Tkinter or PyQt.
- Include performance statistics charts using `matplotlib`.

---

## 💻 How to Run

1. Make sure you have Python installed (recommended version: 3.8 or higher).
2. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Grade-Management-System.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Grade-Management-System
   ```

4. Run the main file:

   ```bash
   python grade_management_system.py
   ```

5. Explore the interactive menu to validate, calculate, and analyze grades.

---
