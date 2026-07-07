# Python Day 03 - Functions Solutions

# Q1
def hello_world():
    print("Hello, World!")


# Q2
def greet(name):
    print("Hello,", name)


# Q3
def square(num):
    return num * num


# Q4
def add(a, b):
    return a + b


# Q5
def print_numbers():
    for i in range(1, 11):
        print(i)


# Q6
def cube(num):
    return num * num * num


# Q7
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Q8
def largest_two(a, b):
    if a > b:
        return a
    else:
        return b


# Q9
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Q10
def multiplication_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


# Q11
def is_prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime"


# Q12
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


# Q13
def reverse_string(text):
    return text[::-1]


# Q14
def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"


# Q15
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            count += 1

    return count


# Q16
def largest_in_list(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


# Q17
def smallest_in_list(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


# Q18
def sum_list(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


# Q19
def remove_duplicates(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique


# Q20
def second_largest(numbers):
    unique = remove_duplicates(numbers)

    largest = unique[0]
    second = unique[0]

    for num in unique:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


# Q21
def calculator(a, b, choice):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid choice"


# Q22
def count_upper_lower(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("Uppercase:", upper)
    print("Lowercase:", lower)


# Q23
def char_frequency(text):
    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


# Q24
def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


# Q25
def menu_program(choice, num):
    if choice == 1:
        return square(num)
    elif choice == 2:
        return cube(num)
    elif choice == 3:
        return even_odd(num)
    elif choice == 4:
        return is_prime(num)
    elif choice == 5:
        return "Exit"
    else:
        return "Invalid choice"