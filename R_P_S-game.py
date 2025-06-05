
# %%

# Rock Paper Scissor Game
import random

def play_game():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    print("Rock, Paper, or Scissors?")
    player = input("Your choice: ").lower()

    if player not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
play_game()

# %%
