![grade_management_system](https://github.com/user-attachments/assets/ed9b3ea0-8f49-4d76-85a3-c729db431a72)

# 📊 Grade Management System

## 📌 Project Description

This project is part of **Module 1 – Week 2 of the training program**, and its goal is to develop an interactive Python system to manage student grades and analyze performance statistics in a simple and functional way.

---

## 🎯 Features

- Validate an individual grade (from 0 to 100) and determine if the student passes (≥ 60).
- Input a list of valid grades separated by commas.
- Calculate the average of the entered grades.
- Count how many grades are greater than a specific value.
- Check if a specific grade exists in the list and how many times it appears.

---

## 🧠 Logic Implemented

- Conditional structures (`if`, `if-else`, `if-elif-else`) are used to validate and evaluate user input.
- `for` and `while` loops are used to navigate lists, control the menu, validate inputs, and count values.
- `break` and `continue` are used to optimize flow control.
- Each functionality is encapsulated in reusable functions to keep the code clean and organized.

---

## ✅ Validations Performed

- Validation of correct range for each grade (0-100).
- Handling of invalid inputs using `try-except`.
- Filtering out invalid entries from lists before processing.
- Considered cases:
  1. Non-numeric inputs
  2. Grades out of range
  3. Empty lists
  4. Detection of duplicates
  5. Verification of a specific grade in the list

---

## 📁 Code Structure

- Code is divided into functions for: individual validation, average calculation, counting, and verification.
- A main menu that directs to each feature.
- Clear comments explaining each section of the code.

---

## 🧩 Technical Justification

The code is built in a modular way to facilitate maintenance and scalability:

- `float()` is used to support decimal grades.
- Flow control structures enable smooth navigation.
- Robust data validation and user feedback were prioritized.
- Menu organization and functional separation allow easy extension of features.

---

## 🚀 Future Improvements

- Export/import grade lists to/from external files (CSV, JSON).
- Add features to edit or delete grades.
- Implement a graphical interface using Tkinter or PyQt.
- Include statistical graphs using `matplotlib`.

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
