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
