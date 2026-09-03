# Python Functions Mastery 🐍

A practical, job-oriented journey to mastering Python functions from beginner to advanced level.

## Day 01 — Function Fundamentals

### Topics Covered

* Why functions are important
* Creating and calling functions
* Parameters and arguments
* Positional arguments
* Keyword arguments
* Default arguments
* `return` vs `print()`
* Passing returned values between functions
* Basic function design
* Single Responsibility Principle

### Practical Exercises

#### 1. Salary Calculator

Created reusable functions to calculate employee salary components such as HRA and DA.

#### 2. Student Result Calculator

Created separate functions for calculating percentage and checking pass/fail status.

#### 3. Employee Management

Practiced positional and keyword arguments while creating employee records.

#### 4. Product Management

Practiced default arguments and overriding default values.

## Key Learning

One of my biggest takeaways today was understanding the difference between `print()` and `return`.

`print()` displays a value, while `return` sends a value back to the caller so it can be stored, reused, or processed further.

I also learned how to design functions with a clear responsibility and pass data from one function to another.

## Progress

Day 01 completed ✅

Currently learning:
# Day 02 — Advanced Python Function Arguments 🐍

Today I continued my practical journey toward mastering Python functions.

## Topics Covered

- Mutable default arguments
- Why mutable default arguments can cause unexpected behavior
- Using `None` to safely handle mutable defaults
- `*args`
- Variable-length positional arguments
- `*args` as a tuple
- Positional argument unpacking using `*`
- `**kwargs`
- Variable-length keyword arguments
- `**kwargs` as a dictionary
- Dictionary unpacking using `**`
- Combining normal parameters, `*args`, and `**kwargs`
- Keyword-only parameters
- Argument ordering rules
- Multiple return values
- Tuple unpacking

## Key Concepts

### Mutable Default Arguments

Learned why using mutable objects such as lists as default parameter values can cause data to persist between function calls.

Instead of:

```python
def add_item(item, items=[]):
    ...
Python Functions — Beginner → Advanced → Professional

More exercises, debugging challenges, advanced concepts, and a real-world function-based project will be added as I progress.

#Python #PythonProgramming #LearningInPublic #SoftwareDevelopment
# Day 03 — Scope, Lambda & Higher-Order Functions 🐍

Today I continued my practical journey toward mastering Python Functions.

The focus was on understanding how Python handles variables inside different scopes and how functions can be treated as objects and passed to other functions.

---

## 📚 Topics Covered

### 1. Scope

Learned how the accessibility of a variable depends on where it is created.

Topics practiced:

- Local scope
- Global scope
- Enclosing scope
- Built-in scope
- Variable shadowing

---

## 2. LEGB Rule

Python searches for variables in this order:
# Day 03 — Scope, Lambda & Higher-Order Functions 🐍

Today I continued my practical journey toward mastering Python Functions.

## 📚 Topics Covered

### Scope & LEGB
- Local Scope
- Global Scope
- Enclosing Scope
- Built-in Scope
- Variable Shadowing
- LEGB Rule
- `global` keyword
- `nonlocal` keyword
- `UnboundLocalError`

### Lambda Functions
- Creating lambda functions
- Lambda with multiple parameters
- Conditional expressions in lambda
- When to use lambda

### Higher-Order Functions
- Passing functions as arguments
- Using functions as parameters
- Creating reusable functions that accept other functions

### `map()`
Used to transform every element of an iterable.

```python
numbers = [2, 4, 6, 8, 10]

result = list(map(lambda x: x * 2, numbers))

print(result)

```text
L → Local
E → Enclosing
G → Global
B → Built-in
# Employee Management & Payroll System

A console-based **Employee Management & Payroll System** built with Python to practice and apply core Python programming concepts, especially functions and functional programming techniques.

This project was developed as a hands-on learning project to understand how different Python concepts can be combined to build a practical application.

---

## 🚀 Features

The application currently provides the following functionality:

* Add new employees
* Display all employees
* Search employees by ID
* Calculate salary with a 10% bonus
* Filter employees based on salary
* Sort employees by salary
* Handle employees that are not found
* Console-based user interaction

---

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Lambda functions
* `filter()`
* `sorted()`
* Loops
* Conditional statements
* Exception-safe input handling
* Return values and `None`

---

## 📚 Python Concepts Practiced

This project was created after learning and practicing the following Python concepts:

### Functions

* Function creation and calling
* Parameters and arguments
* Default and keyword arguments
* `*args` and `**kwargs`
* Multiple return values
* Scope and LEGB
* `global` and `nonlocal`

### Functional Programming

* Lambda functions
* Higher-order functions
* `filter()`
* `map()`
* `sorted()`
* `reduce()`

### Advanced Function Concepts

* Nested functions
* Closures
* Decorators
* `functools.wraps`
* Recursion
* Generators
* `yield`
* Function annotations
* Positional-only arguments
* Keyword-only arguments

Not every concept learned was forced into the project. Concepts were used where they were appropriate for the application's functionality.

---

## 🖥️ Application Workflow

The application follows a simple console-based workflow:

```text
Start Application
       ↓
Add Employee
       ↓
Display Employees
       ↓
Search Employee
       ↓
Calculate Salary + Bonus
       ↓
Filter Employees
       ↓
Sort Employees
       ↓
Exit
```

---

## 📊 Example Employee Data

The application stores employee information using Python dictionaries inside a list.

Example:

```python
employees = [
    {
        "id": 1,
        "name": "Sanjay HM",
        "age": 22,
        "department": "Development",
        "salary": 50000.0
    }
]
```

---

## 💰 Salary Calculation

The application calculates a **10% bonus** based on the employee's salary.

For example:

```text
Salary: ₹50,000
Bonus: ₹5,000
----------------
Total: ₹55,000
```

---

## 🔎 Employee Search

Employees can be searched using their employee ID.

If an employee exists:

```text
Enter employee ID: 1

ID: 1
Name: Sanjay HM
Age: 22
Department: Development
Salary: 50000.0
```

If the employee does not exist:

```text
Enter employee ID: 99

Employee not found
```

---

## 🔍 Salary Filtering

The project uses `filter()` with a lambda function to find employees whose salary meets a specified minimum.

Example:

```python
filtered_employees = filter(
    lambda emp: emp["salary"] >= minimum_salary,
    employees
)
```

If the minimum salary is ₹50,000, employees earning ₹50,000 or more are displayed.

---

## 📈 Employee Sorting

The project uses `sorted()` with a lambda function to sort employees according to their salary.

Example:

```python
sorted_employees = sorted(
    employees,
    key=lambda emp: emp["salary"]
)
```

This allows employees to be displayed from the lowest salary to the highest salary.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project

```bash
cd Employee-Management-System
```

### 3. Run the Python application

```bash
python console-based_Python_application.py
```

---

## 📁 Project Structure

```text
Employee-Management-System/
│
├── console-based_Python_application.py
└── README.md
```

---

## 🎯 Learning Objective

The main objective of this project was to move beyond individual Python exercises and understand how Python concepts work together inside a complete application.

Through this project, I practiced:

```text
Python Basics
     ↓
Functions
     ↓
Functional Programming
     ↓
Data Handling
     ↓
Application Logic
     ↓
Console Application
```

---

## 🔮 Future Improvements

This project will be improved as I learn more Python concepts.

Planned improvements include:

* Convert the application to an OOP-based design
* Introduce classes and objects
* Add encapsulation
* Implement inheritance
* Implement polymorphism
* Add abstraction
* Add proper exception handling
* Store employee data permanently
* Add database integration
* Add a graphical or web interface
* Add automated testing
* Improve project architecture

---

## 👨‍💻 Author

**Sanjay HM**

This project is part of my journey toward becoming a professional Python developer.

---

## ⭐ Project Status

**Completed — Initial Version**

The current version focuses on Python functions and functional programming concepts. Future versions will evolve as I progress into Object-Oriented Programming, databases, APIs, and backend development.
