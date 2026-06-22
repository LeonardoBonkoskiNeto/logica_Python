#######largest number########
def get_number(message):
   while True:
      try:
         return float(input(message))
      except ValueError:
         print("please type only numbers")
while True:
 
  print("The largest number!!!!!")

  n1 = get_number("type number one: ")
  n2 = get_number("type number two: ")

  if n1 > n2:
     print(n1, "it's largest than: ", n2)
  elif  n1 == n2:
      print(n1, "it's equal than: ", n2)
  else:
     print(n2, "it's largest than: ", n1)
     break 
  
  answear = input("try another numbers(y/n): ")
  if answear.lower() == "n":
     break
      