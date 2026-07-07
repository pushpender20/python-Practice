# Python Day 03 - Functions

## Objective

Learn how to write reusable code using functions.

---

# What is a Function?

A function is a block of code that performs a specific task.

Instead of writing the same code again and again, we create a function and call it whenever needed.

Syntax:

```python
def function_name():
    print("Hello World")
```

Calling the function:

```python
function_name()
```

---

# Function with Parameters

Parameters allow us to pass data into a function.

```python
def greet(name):
    print("Hello", name)

greet("Pushpender")
```

Output

```
Hello Pushpender
```

---

# Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(5, 10)
```

---

# Return Statement

A function can return a value.

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
```

---

# Difference Between print() and return

print()

- Displays output.
- Does not send a value back.

return

- Sends a value back to the caller.
- Can be stored in a variable.

Example

```python
def square(x):
    return x * x

ans = square(5)
print(ans)
```

---

# Default Parameters

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rahul")
```

---

# Local Variables

Variables created inside a function.

```python
def demo():
    x = 10
    print(x)
```

---

# Global Variables

Variables declared outside a function.

```python
x = 100

def demo():
    print(x)

demo()
```

---

# Function Calling Function

```python
def greet():
    print("Hello")

def welcome():
    greet()
    print("Welcome")

welcome()
```

---

# Topics Covered

- Functions
- Parameters
- Arguments
- Return
- Default Parameters
- Local Variables
- Global Variables