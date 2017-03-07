 #New dice game

from random import randint 

print("This is a dice rolling game. Each player will roll and who ever gets this highest score out of 3 games wins")

winNumber = 2

playerOne = raw_input("what is your name player one? ")
playerTwo = raw_input("What is your name player two? ")

playerOneWin = 2
#player one value needs to be updated
playerTwoWin = 2

playerOneRoll = randint(1, 20)
playerTwoRoll = randint(1, 20)

Roll = raw_input("press enter to roll")
rollOne = randint(1, 20)
rollTwo = randint(1, 20)

while(playerOneWin != winNumber and playerTwoWin != winNumber):
	playerOneRoll = rollOne
	print(playerOne)
	if(playerOneRoll < playerTwoRoll):
		print("Player one won that round")
		if(playerTwoRoll < playerOneRoll):
			print("Player two won that round")
	playerTwoRoll = rollOne
print(playerOneRoll, playerTwoRoll)

