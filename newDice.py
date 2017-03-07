 #New dice game

 from random import randint 

print("This is a dice rolling game. Each player will roll and who ever gets this highest score out of 3 games wins")

winNumber = 2

playerOne = raw_input("what is your name player one? ")
playerTwo = raw_input("What is your name player two? ")

playerOneWin = 0
playerTwoWin = 0

Roll = raw_input("press enter to roll")
rollOne = randint(1, 20)
rollTwo = randint(1, 20)

while(playerOne != winNumber and playerTwo != winNumber):
	playerOne = randint(1, 20)
	print(playerOne)
	playerTwo = randint(1, 20)
	print(playerTwo )
	if(playerOne > playerTwo ):
		print('player one won that round')
		playerOneWin += 1
	if(playerTwo  > playerOne ):
		print("player two won that round")
		playerTwoWin += 1
if(playerOneWin == winNumber):
	print('Congrates player one won the game')
if(playerTwoWin == winNumber):
	print('Congrats player two won the game')