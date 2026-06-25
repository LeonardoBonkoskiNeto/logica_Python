######Mine Bank########

balance = 1000
while True:
    print("\n1 - See balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")

    option = input("Choose: ")

    if option == "1":
        print("Balance: ", balance)

    elif option == "2":
        value = float(input("Value to deposit: "))
        if value <= 0:
            print("Please enter a positive value!!!")
        else:
         balance += value
        print("New Balance is:  ", balance)

    elif option == "3":
         value = float(input("Value to withdraw: "))

         if value <= 0:
            print("Please enter a positive value!!!")
            
         elif value <= balance:
          balance -= value 
          print("New balance is: ", balance)
         else:
             print("Insufficiant funds")

    else:
        print("End of transation...")
        break
