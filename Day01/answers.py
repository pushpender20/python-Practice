#Q1
print("hello world")

#Q2
name = "pushpender thakur"
print(name)

#Q3
age = 22
city = "new york"
print("my name is", name, ", my age is", age, "and i live in", city)

#Q4
name=input("enter your name: ")
print("hello", name)

#Q5
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=a+b
print(c)

#Q6
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
add=a+b
sub=a-b
mul=a*b
div=a/b
print(add)
print(sub)
print(mul)
print(div)

#Q7
age=int(input("Enter your age: "))
print("your age is", age)

#Q8
name="pushpender"
age=22
hieght=5.9
is_student=True
print("my name is", name, ", my age is", age, ", my hieght is", hieght, "and i am a student:", is_student)

#Q9
a=5
b=5.5
c="hello"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Q10
a=5
b=10
c=a
a=b
b=c
print("value of a is", a)
print("value of b is", b)

#Q11
a=5
b=10
a,b=b,a
print("value of a is", a)
print("value of b is", b)

#Q12
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)

#Q13
radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area =", area)

#Q14
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total =", total)
print("Percentage =", percentage)

#Q15
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

#Q16
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)

print("Largest number =", largest)

#Q17
birth_year = int(input("Enter your birth year: "))

current_year = 2026

age = current_year - birth_year

print("Your age is", age)

#Q18
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q19
monthly_salary = float(input("Enter monthly salary: "))

yearly_salary = monthly_salary * 12

print("Yearly Salary =", yearly_salary)

#Q20
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)