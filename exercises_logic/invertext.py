#inverter of texts#############
while True:
    text = input("type a word: ")

    inverted = ""

    for letter in text:
        inverted = letter + inverted

    print(inverted)
    
    answear = input("would you like to type other word?(y/n): ")

    if answear == "n":
       print("end of the program!!!!!!")
       break