#main page

#import these classes from the other two modules
from guessNumber import startGame
from playerDetails import playerDetails

# create player
player = playerDetails()
player.playerName()

#start game
game = startGame(player)
game.runGame()
