#Define the grid 3*3

y_grid = 1

#direction = str(input("Direction: "))

def go_north(y):
    y += 1
    return y

y_grid = go_north(y)

x = 1
y = 1 


print("You can travel: (N) orth.")


#Starts in (1,1)
#Displays the directions for which there are adjacent tiles that the player can travel to in each round
#Enters the first letter for the direction player wants to go to. Capitalized or small 
#If the player enters invalid direction, print "Not a valid direction!" and allows the player to enter the direction again
#Tile (3,1) is the victory location. When entered progra notifies player of their victory and quits running


