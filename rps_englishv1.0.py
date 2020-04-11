#Copyright (c) 2020 Welton Felix
#
# This file is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import random
##############
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
lizard = "Lizard"
spock = "Spock"
possibleChoices = [rock, paper, scissors, lizard, spock]
winner = False 
stop = False 
pcPoints = 0 
userPoints = 0 
stopOptions = ["Stop", "Exit","Break", "Leave"] # Stop key-words
while stop == False:
  pcChoice = possibleChoices[random.randint(0,2)] # The array position is randomized: 0 = Rock, 1 = Paper and 2 = Scissors (PC can't choose neither lizard nor Spock)
  userChoice = (input("Rock, Paper, Scissors, Shoot!").lower()).capitalize() 
  # LOGICAL TESTS
  if userChoice in stopOptions:
    stop = True
    print("-----GAME OVER-----")
    print("Points: ")
    print("PC:   " + str(pcPoints) + ' pts.')
    print("You: " + str(userPoints) + ' pts.')
    if pcPoints > userPoints:
      print("Computer wins. Better luck next time.")
    elif userPoints > pcPoints: 
      print("Congratulations!! You win!")
    else: #(Pontos iguais)
      print("Tie!")
    print("---------------------")
    exit = input("Press enter to exit") # The user can exit application, but can still read end messages
  elif userChoice in possibleChoices: 
    print("Computer chose " + pcChoice + " and You chose " + userChoice + ".")
    if pcChoice != userChoice:
      if pcChoice == rock or userChoice == rock:
        if pcChoice == paper or userChoice == paper:
          action = "covers"
          if pcChoice == paper:
            winner = "pc"
        elif pcChoice == scissors or userChoice == scissors:
          action = "crushes"
          if pcChoice == rock:
            winner = "pc"
        elif userChoice == lizard:
          action = "crushes"
          winner = 'pc'
        elif userChoice == spock:
          action = 'vaporizes'
      elif pcChoice == paper or userChoice == paper:
        if userChoice == spock:
          action = 'disproves'
          winner = 'pc'
        elif pcChoice == scissors or userChoice == scissors:
          action = "cuts"
          if pcChoice == scissors:
            winner = "pc"
        elif userChoice == lizard:
          action = 'eats'
      elif userChoice == spock:
        if pcChoice == scissors:
          action = 'smashes'
      elif userChoice == lizard:
        if pcChoice == scissors:
            action = 'decapitates'
            winner = 'pc'
      if userChoice == spock or userChoice == lizard:
        print("Congratulations! You found an easter egg from The Big Bang Theory")
      if winner:
        print(pcChoice + ' ' + action + ' ' + userChoice + ', PC wins!')
        pcPoints += 1
      else:
        print(userChoice + ' ' + action + ' ' + pcChoice + ', you win!')
        userPoints += 1
    else:
      print("Tie!")
  else:
    print("Ops, you have chosen an invalid object")
  winner = False # Resets winner
  print(' ')
  print("========================================")
  print('PC: ' + str(pcPoints) + ' points  You: ' + str(userPoints) + ' points')
  print('========================================')
  print(' ')
