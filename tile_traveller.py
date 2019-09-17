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


n = "(N) orth"
s = "(S) outh"
e = "(E) ast" 
w = "(W) est"



while x_grid != 2 and y_grid != 2:

    if y_grid == 1 and x_grid == 1:
        print("You can travel: " + n + ".")

    direction = input("Direction: ")
    if direction == "n" or "N":
        y_grid = go_north(y_grid)
    elif direction == "s" or "S":
        y_grid = go_south(y_grid)
    elif direction == "e" or "E":
        x_grid = go_east(x_grid)
    elif direction == "w" or "W":
        x_grid = go_west(x_grid)
    else:
        print("Not a valid direction!")
        continue
else:
    print("Victory!")
#direction = str(input("Direction: "))



print("(" + str(x_grid) + ", " + str(y_grid) + ")")


#Starts in (1,1)
#Displays the directions for which there are adjacent tiles that the player can travel to in each round
#Enters the first letter for the direction player wants to go to. Capitalized or small 
#If the player enters invalid direction, print "Not a valid direction!" and allows the player to enter the direction again
#Tile (3,1) is the victory location. When entered progra notifies player of their victory and quits running

