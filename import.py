import random
while True:
    choices = ["rock","paper","scissors"]

    CPU = random.choice(choices)
    player=None

    while player not in choices:

        player = input(" [R = rock], [P= paper], or [S =scissors?]: ")

    if player == CPU:
        print("CPU", "player")
        print("Ties!")
    elif player == "rock":
       if CPU == "paper":
          print("CPU:paper", "player:rock")
    
          print("You lose!")
       if CPU == "scissors":
          print("computer: scissors", "player:rock ")
          
          print("You win!")
    elif player == "scissors":
       if CPU == "rock":
          print("CPU:rock", "player:scissors")
          
          print("You lose!")
       if CPU == "paper":
          print("CPU:paper", "player:scissor")
          
          print("You win!")
    elif player == "paper":
       if computer == "scissors":
          print("CPU: scissors", "player:paper")
          
          print("You lose!")
       if CPU == "rock":
          print("CPU:rock", "player:paper")
          
          print("You win!")



    play_again = input("play again? (yes/no): ")

    if play_again !="yes":
     break
    
print("Bye!")










