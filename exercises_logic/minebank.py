######Mine Bank########

balance = 1000
seccond_account = 500
password = "123"
history = []



def type_word(password):
  
  autentication = False 

  while not autentication: 
     word = str(input("Password: "))

     if word == password:
        autentication = True   
        print("Welcome back sir!!!!!!")

     else:
        print("Incorrect password!!!!")

        

def transfer(balance, seccond_account, history):
   try:
      value = float(input("value to transfer: "))

      if value  <= 0:
         print("please try a positive number!")
         return balance
      
      if value <= balance:
         balance -= value

         seccond_account += value

         history.append(f"New transfer from 'Main account' to 'Seccond account': +${value:.2f}")

         print("\nTransfer completed")
         print(f"Main account current balance: ${balance:.2f}")
         print(f"seccond account balance: ${seccond_account:.2f}")

         return balance, seccond_account
   
      else:
         print("inssuficient funds!!!")

         return balance, seccond_account
      
   except ValueError:
      print("Please type a valid number")

      return balance, seccond_account




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


type_word(password)
      

while True:


         print("####### MINE BANK ######3")
         print("\n1 - See balance")
         print("2 - Deposit")
         print("3 - Withdraw")
         print("4 - Transaction history")
         print("5 - transfer")
         print("6 - Exit")

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
               balance, seccond_account = transfer(balance, seccond_account, history)

         elif option == "6":
              print("End of transaction")
         else:
            print("Error...")
            break
