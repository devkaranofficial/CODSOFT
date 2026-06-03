import random
choices = ["Rock" , "Paper" , "Scissor"]
computer_wins = 0
user_wins = 0

while True:
    print("Rock Paper Scissor Game")
    print("1)Rock")
    print("2)Paper")
    print("3)Scissor")
    print("4)ScoreBoard")
    print("5)Exit")


    #Choice
    try:
        user_choice = int(input("\nEnter Your Choice:"))
    except ValueError:
        print("Enter Valid Input(1-5)!\n")
        continue
    if user_choice == 5:
        print("Program Exited Succesfully!\n")
        break
    
    #Printing user and computer choice
    if user_choice > 0 and user_choice < 5 and user_choice != 4:
        if user_choice == 1:
            user_draws = "Rock"
        elif user_choice == 2:
            user_draws = "Paper"
        elif user_choice == 3:
            user_draws = "Scissor"
    

        computer_choice =random.choice(choices)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if user_choice == 1:
            print(f"You chose : Rock")
        elif user_choice == 2:
            print(f"You chose : Paper")
        elif user_choice == 3:
            print(f"You chose : Scissor")
        print(f"Computer Chose : {computer_choice}")
        

        #Rules
        if computer_choice == "Rock" and user_draws == "Paper" or computer_choice == "Paper" and user_draws == "Scissor" or computer_choice == "Scissor" and user_draws == "Rock":
            print("You Win!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            user_wins += 1
        elif computer_choice == "Rock" and user_draws == "Scissor" or computer_choice == "Scissor" and user_draws == "Paper" or computer_choice == "Paper" and user_draws == "Rock":
            print("Computer Wins!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            computer_wins += 1
        else:
            print("Draw! \nTry Again")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    elif user_choice == 4:
        print(f"~~~~~~============Score============~~~~~~\n\tComputer:{computer_wins} \t| \tUser:{user_wins}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Enter Valid Input(1-5)")