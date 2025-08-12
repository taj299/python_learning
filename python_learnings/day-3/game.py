"""
rock paper scissor

user
computer

user choice == computer choice
match tie

rock > paper
paper win

rock > scissor
rock win

"""


 import random
   user_choice = input("Enter your choice [rock/paper/scissor] = ")
   computer_choice = random.choice(["rock", "paper", "scissor"])

   if user_choice == computer_choice:
    print("Match Tied!")
  
   elif user_choice == "Rock":
      if computer_choice == "Scissor"
      print("You won, Rock smashes Scissor")
   else:
    print:("Computer won, Paper covers Rock")

   elif user_choice == "Paper":
     if computer_choice =="rock":
        print("you won,paper covers rock")
    else:
        print("computer won, Scissor cuts paper")
    
    elif user_choice =="Scissor":
        if computer_choice =="Rock":
            print("Computer won, Rock Smashes Scissor")
        else:
            print("You won, scissor cuts paper")
        else:
            print("In-valid input")
