balance=int(input("Enter the amount : "))
Withdraw=int(input("Enter the amount to withdraw: "))
Amount=balance-Withdraw

if Withdraw>balance or Withdraw<=0:
    print("Insufficient balance.")
if Withdraw<=balance and Withdraw>0:
    print("Please collect your cash.Remaining balance is:",Amount)

