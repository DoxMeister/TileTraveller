#Define the grid 3*3


def can_go(n,s,e,w):
    counter = 0
    ret = "You can travel: "

    if n :
        ret += "(N) orth"
        counter += 1

    if s:
        if counter == 1 or 2 or 3 or 4:
            ret += " or "
        ret += "(S) outh"
        counter += 1

    if e:
        if counter == 1 or 2 or 3 or 4:
            ret += " or "
        ret += "(E) ast"
        counter += 1

    if w:
        if counter == 1 or 2 or 3 or 4:
            ret += " or "
        ret += "(W) est"
        counter += 1

    ret += "."

    return print(ret)

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



while True:

    if y_grid == 1 and x_grid == 1:
        can_go(1,0,0,0)
    elif y_grid == 2 and x_grid == 1:
        can_go(1,1,0,0)
    elif y_grid == 3 and x_grid == 1:
        can_go(0,1,1,0)
    elif y_grid == 1 and x_grid == 2:
        can_go(1,0,0,0)
    elif y_grid == 3 and x_grid == 2:
        can_go(0,0,1,1)
    elif y_grid == 1 and x_grid == 3:
        print("Victory!")
        break
    elif y_grid == 2 and x_grid == 3:
        can_go(1,1,0,0)
    elif y_grid == 3 and x_grid == 3:
        can_go(0,0,1,1)
    elif x_grid == 2 and y_grid == 2:
        can_go(0,1,0,1)

    direction = str(input("Direction: "))

    if direction == "n" or direction == "N":
        y_grid = go_north(y_grid)
    elif direction == "s" or "S":
        y_grid = go_south(y_grid)
    elif direction == "e" or "E":
        x_grid = go_east(x_grid)
    elif direction == "w" or "W":
        x_grid = go_west(x_grid)
    else:
        print("Not a valid direction!")

#direction = str(input("Direction: "))



print("(" + str(x_grid) + ", " + str(y_grid) + ")")



#Starts in (1,1)
#Displays the directions for which there are adjacent tiles that the player can travel to in each round
#Enters the first letter for the direction player wants to go to. Capitalized or small 
#If the player enters invalid direction, print "Not a valid direction!" and allows the player to enter the direction again
#Tile (3,1) is the victory location. When entered progra notifies player of their victory and quits running

