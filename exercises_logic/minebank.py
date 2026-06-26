######Mine Bank########

balance = 1000
history = []

def Show_Balance(balance):
   print(f"Current balance:  ${balance:.2f}")

def Deposit(balance, history):
   try:
      value = float(input("value to deposit: "))
      if value <= 0:
         print("Please type a positive number!!!!")
         return balance
      
      balance += value

      history.append(f"new deposit: +${value:.2f}")

      print(f"New balance:  ${balance:.2f}")
      return balance
   
   except ValueError:
      print("Error!!!",)    
      
def Withdraw(balance, history):
    try:
        value = float(input("Value to withdraw: "))

        if value <= 0:
            print("Please type a positive number!!!")
            return balance

        if value <= balance:
            balance -= value

            history.append(f"New withdraw: -${value:.2f}")

            print(f"Current balance: ${balance:.2f}")
        else:
            print("Insufficient funds")

        return balance

    except ValueError:
        print("Please try a valid number!!!")
        return balance
    
def Show_History(history):
   print("--------Transaction History---------")
   if len(history) == 0:
      print("No transactions found")

   else:
      for transaction in history:
         print(transaction)
      

while True:


    print("####### MINE BANK ######3")
    print("\n1 - See balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Transaction history")
    print("5 - Exit")

    option = input("Choose: ")

    if option == "1":
       Show_Balance(balance)

    elif option == "2":
      balance =  Deposit(balance,history)

    elif option == "3":
        balance = Withdraw(balance, history)

    elif option == "4":
       Show_History(history)

    elif option == "5":
       print("End of transaction")
    else:
        print("Error...")
        break
