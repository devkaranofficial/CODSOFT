while True:

    print("\n~~~~~~~~~~~~ Calculator ~~~~~~~~~~~~")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exponent")
    print("6) Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 6:
        print("Program exited successfully!")
        break

    num_1 = float(input("Enter First Number: "))
    num_2 = float(input("Enter Second Number: "))

    if choice == 1:
        result = num_1 + num_2
        print(f"{num_1} + {num_2} = {result}")

    elif choice == 2:
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}")

    elif choice == 3:
        result = num_1 * num_2
        print(f"{num_1} * {num_2} = {result}")

    elif choice == 4:
        if num_2 != 0:
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result}")
        else:
            print("Division by zero is not allowed!")

    elif choice == 5:
        result = num_1 ** num_2
        print(f"{num_1} ** {num_2} = {result}")

    else:
        print("Invalid Choice!")