import random
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player=None

    while player not in choices:

        player = input("rock,paper, or scissors?: ")

    if player == computer:
        print("computer", computer)
        print("player", player )
        print("Ties!")
    elif player == "rock":
       if computer == "paper":
          print("computer:paper", computer)
          print("player:rock", player)
          print("You lose!")
       if computer == "scissors":
          print("computer: scissors", computer)
          print("player:rock ", player)
          print("You win!")
    elif player == "scissors":
       if computer == "rock":
          print("computer:rock", computer)
          print("player:scissors", player)
          print("You lose!")
       if computer == "paper":
          print("computer:paper", computer)
          print("player:scissor", player)
          print("You win!")
    elif player == "paper":
       if computer == "scissors":
          print("computer: scissors", computer)
          print("player:paper ", player)
          print("You lose!")
       if computer == "rock":
          print("computer:rock", computer)
          print("player:paper", player)
          print("You win!")



    play_again = input("play again? (yes/no): ")

    if play_again !="yes":
     break
    
print("Bye!")










