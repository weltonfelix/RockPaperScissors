#Copyright (c) 2020 Welton Felix
#
# This file is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import random
##############
rock = "Pedra"
paper = "Papel"
scissors = "Tesoura"
lizard = "Lagarto"
spock = "Spock"
possibleChoices = [rock, paper, scissors, lizard, spock]
winner = False 
stop = False 
pcPoints = 0 
userPoints = 0 
stopOptions = ["Parar", "Encerrar","Finalizar", "Pare", "Fim"] # Stop key-words
while stop == False:
  pcChoice = possibleChoices[random.randint(0,2)] # The array position is randomized: 0 = Rock, 1 = Paper and 2 = Scissors (PC can't choose neither lizard nor Spock)
  userChoice = (input("Pedra, Papel ou Tesoura?").lower()).capitalize() 
  # LOGICAL TESTS
  if userChoice in stopOptions:
    stop = True
    print("-----FIM DO JOGO-----")
    print("Pontos: ")
    print("PC:   " + str(pcPoints) + ' pts.')
    print("Você: " + str(userPoints) + ' pts.')
    if pcPoints > userPoints:
      print("O PC ganhou. Mais sorte na próxima.")
    elif userPoints > pcPoints: 
      print("PARABÉNS!! Você ganhou!")
    else: #(Pontos iguais)
      print("Empatou!")
    print("---------------------")
    exit = input("Para sair, aperte enter") # The user can exit application, but can still read end messages
  elif userChoice in possibleChoices: 
    print("O PC escolheu " + pcChoice + " e você escolheu " + userChoice + ".")
    if pcChoice != userChoice:
      if pcChoice == rock or userChoice == rock:
        if pcChoice == paper or userChoice == paper:
          action = "embrulha"
          if pcChoice == paper:
            winner = "pc"
        elif pcChoice == scissors or userChoice == scissors:
          action = "amassa"
          if pcChoice == rock:
            winner = "pc"
        elif userChoice == lizard:
          action = "esmaga"
          winner = 'pc'
        elif userChoice == spock:
          action = 'vaporiza'
      elif pcChoice == paper or userChoice == paper:
        if userChoice == spock:
          action = 'rejeita'
          winner = 'pc'
        elif pcChoice == scissors or userChoice == scissors:
          action = "corta"
          if pcChoice == scissors:
            winner = "pc"
        elif userChoice == lizard:
          action = 'come'
      elif userChoice == spock:
        if pcChoice == scissors:
          action = 'destrói'
      elif userChoice == lizard:
        if pcChoice == scissors:
            action = 'decapita'
            winner = 'pc'
      if userChoice == spock or userChoice == lizard:
        print("Parabéns! Você descobriu uma referência de The Big Bang Theory")
      if winner:
        print(pcChoice + ' ' + action + ' ' + userChoice + ', o PC venceu!')
        pcPoints += 1
      else:
        print(userChoice + ' ' + action + ' ' + pcChoice + ', você venceu!')
        userPoints += 1
    else:
      print("Empate!")
  else:
    print("Ops, você escolheu um objeto inválido")
  winner = False # Resets winner
  print(' ')
  print("========================================")
  print('PC: ' + str(pcPoints) + ' pontos  Você: ' + str(userPoints) + ' pontos')
  print('========================================')
  print(' ')
