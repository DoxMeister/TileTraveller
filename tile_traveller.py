#Define the grid 3*3

def go_north(y):
    y += 1
    return y

def go_south(y):
    y -= 1
    return y

def go_east(x):
    x += 1
    return x

def go_west(x):
    x -= 1
    return x

y_grid = 1
x_grid = 1

print("(" + str(y_grid) + ", " + str(x_grid) + ")")


#direction = str(input("Direction: "))

def go_north(y):
    y += 1
    return y

y_grid = go_north(y)

print("You can travel: (N) orth.")


#Starts in (1,1)
#Displays the directions for which there are adjacent tiles that the player can travel to in each round
#Enters the first letter for the direction player wants to go to. Capitalized or small 
#If the player enters invalid direction, print "Not a valid direction!" and allows the player to enter the direction again
#Tile (3,1) is the victory location. When entered progra notifies player of their victory and quits running

