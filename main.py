from random import choice
objects = ["rock", "paper", "scissors"]
computer = choice(objects)
rps = input("What will you choose? Rock, paper, or scissors?").lower().strip()
if rps == computer:
  print ("It's a tie! :p")
if rps == ("rock"):
    if computer == ("scissors"):
      print ("Yay! You Won! :)")
if rps == ("paper"):
    if computer == ("rock"):
      print ("Yay! You Won! :)")
if rps == ("scissors"):
    if computer == ("paper"):
      print ("Yay! You Won! :)")
if computer == ("scissors"):
  if rps == ("paper"):
    print ("OHHH! You Lost :(")
if computer == ("paper"):
  if rps == ("rock"):
    print ("OHHH! You Lost :(")
if computer == ("rock"):
  if rps == ("scissors"):
    print ("OHHH! You Lost :(")
print ("Thanks for Playing!")
