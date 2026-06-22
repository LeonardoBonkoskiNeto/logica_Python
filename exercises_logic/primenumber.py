##########prime number##############
while True:

    number = int(input("type a number: "))

    prime = True

    print("Antes:", prime)

    if number <= 1:
        prime = False

    for i in range(2, number):
        print("Testando", i)

        if number % i == 0:
            prime = False
            print("Achei divisor:", i)
            break

    print("Depois:", prime)

    answer = input("Try another number? (y/n): ")

    if answer.lower() == "n":
        break