#import random and import from playerDetails moudle 
import random
from playerDetails import playerDetails

#run an instance of the player name class

#create guessing game class
class startGame():

	#Explains the rules
	def rules(self):
		return """Pick a number between 1 -100, if you are correct you win the game. 
		"If you guess wrong you get 5 more chances to get it right. 
		"Every time you guess wrong you lose a life. But you are prompted whether the number is higher or lower. 
		"If your Lives hit 0 you will lose the game. 
		"Good Luck!!! ;) """

	#Initialise and create an instance of the palyers details
	def __init__(self, player):
		self.number = random.randint(1, 100) #randomiser number function between the numbers 1 - 100 
		self.player = player #stores the values from the player detail class

	#function starts the game
	def runGame(self):

		print(f"Welcome {self.player.name} !")
		print(self.rules())
		print("Guess a number between 1 and 100: ")

		#once the player enters a name it prints the rules and asks the player to guess the number
		#The loop will run once the player has more than 0 lives
		while self.player.lives > 0:

			#player is prompted to eter a number
			playersGuess = int(input("Guess a number: "))

			#If the player guesses the right number then the are presented with this message 
			if playersGuess == self.number:
				print( f"Congragualtions {self.player.name}, you guessed the correct number!! Thank you for playing. Goodbye") #includes the player name
				break

			#if the player gueses too low then they are presented with this messages and lose a life 
			elif playersGuess < self.number:
				print("Incorrect, number is too low! Guess again!")
				self.player.loseLife() 
				print(f"Lives remaining: {self.player.lives}")

			#if the player gueses too high then they are presented with this messages and lose a life 
			elif playersGuess > self.number:
				print("Incorrect, number is too high! Guess again")
				self.player.loseLife()
				print(f"Lives remaining: {self.player.lives}")

			#if the user doesn't enter a number they are presented with this 
			else:
				print("Not a number Please enter a number!")
				break

			#player gets this message if they loose
			if self.player.lives == 0:
				print(f"The number was {self.number}")
				print("Game, Over Mate!")
			
