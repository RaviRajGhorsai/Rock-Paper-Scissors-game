import random
end = 'y'
while(end != 'n'):
    user_action = input("Enter your move:  ")

    possible_action = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_action)

    print(f"You choose {user_action} and computer choose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both player selected {user_action} so it's a tie.\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors. So you win!!\n")
        else:
            print("Paper covers rock. So you lose..\n")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock. So you win!!\n")
        else:
            print("Scissors cuts paper. So you lose..\n")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper. So you win!!\n")
        else:
            print("Rock smashes scissors. So you lose..")
    end = input("Do you want to play again: Y/N:  ")