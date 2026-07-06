# Python Day 02 - Conditional Statements

## Topics Covered

- if Statement
- if-else Statement
- if-elif-else Statement
- Nested if
- Comparison Operators
- Logical Operators
- Real-world Decision Making

---

# 1. if Statement

The `if` statement executes a block of code only when the condition is True.

Syntax

```python
if condition:
    # code
```

Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

Output

```
Eligible to vote
```

---

# 2. if-else Statement

When the condition is False, the `else` block executes.

Syntax

```python
if condition:
    # code
else:
    # code
```

Example

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# 3. if-elif-else Statement

Used when multiple conditions need to be checked.

Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

Example

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

# 4. Nested if

An if statement inside another if statement.

Example

```python
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

---

# 5. Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

Example

```python
if salary > 50000:
    print("High Salary")
```

---

# 6. Logical Operators

## AND

Both conditions must be True.

```python
if age >= 18 and citizen:
    print("Eligible")
```

---

## OR

At least one condition must be True.

```python
if city == "Delhi" or city == "Shimla":
    print("Selected")
```

---

## NOT

Reverses the condition.

```python
if not is_raining:
    print("Go Trekking")
```

---

# Indentation

Python uses indentation instead of braces.

Correct

```python
if age >= 18:
    print("Adult")
```

Incorrect

```python
if age >= 18:
print("Adult")
```

---

# Common Beginner Mistakes

❌ Using = instead of ==

Wrong

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

❌ Forgetting colon

Wrong

```python
if age >= 18
```

Correct

```python
if age >= 18:
```

---

❌ Incorrect indentation

Always indent the code inside if, elif and else.

---

# Best Practices

- Use meaningful variable names.
- Keep conditions simple.
- Use elif instead of multiple if statements when checking related conditions.
- Indent consistently using 4 spaces.

---

# Key Takeaways

- if executes only when the condition is True.
- else executes when the if condition is False.
- elif checks additional conditions.
- Nested if is used for multiple levels of decision-making.
- Logical operators combine conditions.