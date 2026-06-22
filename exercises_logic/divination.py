import random 

secret_number =  random.randint(1,100)

while True:
    divinenumber = int(input("guess the number: "))

    if divinenumber < secret_number:
            print("higher")

    elif divinenumber > secret_number:
            print("lower!")
        
    else:
            print("congrats you win!!!!")
            break
