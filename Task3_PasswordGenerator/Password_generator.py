import random
import string
characters = string.ascii_letters + string.digits + string.punctuation

while True:
        choice = input("Would You Like to generate a Password(y/n):")
        if choice.lower() == "y":
            password = ""
            try:
                length  = int(input("Enter Length of the password:"))
                for i in range(length):
                 password += random.choice(characters)
                print(f"The generated Password is {password}")
            except ValueError:
                print("Please enter a valid number!")
        elif choice.lower() == "n":
            print("Program Exited Succesfully!\nThank You")
            break
        else:
            print("Enter Correct Input!")
