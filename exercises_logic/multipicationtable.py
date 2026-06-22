############Multiplication Table########################
while True:
    number = int(input("choose a number for his table: "))

    for i in range(1,11):
     print(number,"X", i, "=", number * i)