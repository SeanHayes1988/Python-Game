#This moudle will ask the player for their name and give them 6 lives
class playerDetails:

	#get the user to enter there name function
	def playerName(self):
		self.name =  input("Please enter your name: ")

	#this funtion will welcome the player by name 
	def welcomePlayer(self):
		return f"Hello {self.name}, and welcome to the game!"

	#function gives the player an intial 6 lives
	def __init__(self):
		self.lives = 6

	#this function will subtract one live when the player guesses wrong
	def loseLife(self):
		self.lives -= 1
        
