from random import randint

choices = ["Rock", "Paper", "Scissors"]
computer_wins = 0
player_wins = 0

while True:
    player_choice = input("Choose Rock, Paper, or Scissors (or enter 'quit' to exit): ")
    if player_choice == "quit":
        break

    comp_choice = choices[randint(0, 2)]

    if player_choice == comp_choice:
        print("It's a tie!")
    elif player_choice == "Rock":
        if comp_choice == "Paper":
            print("You lose! Computer chose", comp_choice, "and you chose", player_choice)
            computer_wins += 1
        else:
            print("You win! You chose", player_choice, "and computer chose", comp_choice)
            player_wins += 1
    elif player_choice == "Paper":
        if comp_choice == "Scissors":
            print("You lose! Computer chose", comp_choice, "and you chose", player_choice)
            computer_wins += 1
        else:
            print("You win! You chose", player_choice, "and computer chose", comp_choice)
            player_wins += 1
    elif player_choice == "Scissors":
        if comp_choice == "Rock":
            print("You lose! Computer chose", comp_choice, "and you chose", player_choice)
            computer_wins += 1
        else:
            print("You win! You chose", player_choice, "and computer chose", comp_choice)
            player_wins += 1
    else:
        print("Invalid input!")

    print("Score:")
    print("Computer wins:", computer_wins)
    print("Player wins:", player_wins)
    print()
        