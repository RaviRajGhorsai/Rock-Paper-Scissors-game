import random
end = 'y'

while(end != 'n'):
    possible_action = ["rock", "paper", "scissors"]
    user_action = None
    while user_action not in possible_action:
        user_action = input("Enter your move:  ").lower()

    computer_action = random.choice(possible_action)

    print(f"Player: {user_action}\ncomputer: {computer_action}.\n")

    if user_action == computer_action:
        print("Tie!!\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!!\n")
        else:
            print("You lose..\n")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!!\n")
        else:
            print("You lose..\n")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!!\n")
        else:
            print("You lose..")
    end = input("Do you want to play again: Y/N:  ").lower()