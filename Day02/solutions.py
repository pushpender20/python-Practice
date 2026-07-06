#Q1


a=int(input("Enter a number: "))
if a>0:
    print("The number is positive.")
elif a<0:
    print("The number is negative.")
else:
    print("The number is zero.")



#Q2
a=int(input("Enter a number: "))
if(a%2==0):
    print("The number is even.")
else:
    print("The number is odd.")


#Q3
age=int(input("Enter a number: "))
if age>=18:
    print("The person is eligible to vote.")
else:
    print("The person is not eligible to vote.")


#Q4
age=int(input("Enter a number: "))
if age>=18:
    print("The person is eligible for a driving licence")
else:
    print("The person is not eligible for a driving licence")


#Q5
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a>=b:
    print("The first number is greater than or equal to the second number.")
else:
    print("The first number is less than the second number.")


#Q6
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))
if a>=b and a>=c:
    print("The first number is the greatest.")
elif b>=a and b>=c:
    print("The second number is the greatest.")
else:
    print("The third number is the greatest.")



#Q7
a=int(input("Enter a number: "))

if a>=90 and a<=100:
    print("A")
elif a>=75 and a<=89:
    print("B")
elif a>=50 and a<=74:
    print("C")
else:
    print("F")


#Q8
Year=int(input("Enter a Year: "))
if Year%4==0 and Year%100!=0 or Year%400==0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year")


#Q9
Salary=int(input("Enter a Salary: "))
if Salary>=70000:
    print("High Salary")
else:
    print("Average Salary")



#Q10
City=input("Enter a City: ")
if City=="Shimla" or City=="Delhi" or City=="Chandigarh" or City=="Shimla":
    print("Service is available")
else:
    print("Not available")



#Q11
Marks=int(input("Enter a marks: "))
attendance=int(input("Enter attendance: "))
if(marks>=40 and attendance>=75):
    print("The student is passed.")
else:
    print("The student is not passed.")


#Q12
Age=int(input("Enter your age: "))
if Age>=18 and Age<=45:
    print("person is elligible.")
else:
    print("person is not elligible.")




#Q13
username=input("Enter your username: ")
password=input("Enter your password: ")
if username=="admin" and password=="python123":
    print("user can login")
else:
    print("user cannot login")


#Q14
age=int(input("Enter your age: "))
citizenship=input("Enter your citizenship: ")
if age>=18 and citizenship=="Indian":
    print("person is eligible to vote.")
else:
    print("person is not eligible to vote.")


#Q15
Temperature=int(input("Enter the temperature: "))
if Temperature>35:
    print("hot")
elif Temperature<35 and Temperature>20:
    print("pleasant")
else:
    print("cold")


#Challenge 1

balance=int(input("Enter the amount : "))
Withdraw=int(input("Enter the amount to withdraw: "))
Amount=balance-Withdraw

if Withdraw>balance or Withdraw<=0:
    print("Insufficient balance.")
if Withdraw<=balance and Withdraw>0:
    print("Please collect your cash.Remaining balance is:",Amount)


#challenge 2
age=int(input("Enter your age: "))
if age<12:
    print("Child")
elif age>=12 and age<18:
    print("Teenager")
elif age>=18 and age<60:
    print("Adult")
elif age>=60:
    print("Senior Citizen")


#challenge 3
bill=int(input("Enter your bill amount: "))
if bill>=2000:
    print("You will get a 20% discount on your bill. bill=",bill-(bill*20/100))
elif bill>=1000 and bill<2000:
    print("You will get a 10% discount on your bill. bill=",bill-(bill*10/100))
else:
    print("You will not get any discount on your bill. bill=",bill)
