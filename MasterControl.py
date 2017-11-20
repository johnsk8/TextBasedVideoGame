# Master Control file for the text-based game
# Author: John L Garcia

import Layout
import os, pickle


def save(userName, className, classGun, classGunDamage, classStats):
    print("\nSaving character:", userName)
    print("Please wait...")

    # Need to save: username, className, classStats
    charDict = {"Name": userName, "Class": className, "Gun": classGun, "Gun Damage": classGunDamage, "Stats": classStats}

    curDir  = os.path.realpath(os.path.dirname(__file__)) 	    # Current directory
    savesDir = os.path.join(curDir, "Saves") 		            # Saves directory
    fname = os.path.join(savesDir, userName + ".pkl") 	        # Make pickle file

    with open(fname, "wb") as saveFile:                         # Write the pickle file here
        pickle.dump(charDict, saveFile)

    print("\nSaved!")
    return


def load():
    # Go through save files and print usernames
    curDir  = os.path.realpath(os.path.dirname(__file__)) 	# Current directory
    savesDir = os.path.join(curDir, "Saves") 		        # Saves directory

    n = 1 # Number of saved characters in list
    for filename in os.listdir(savesDir):
        print(str(n) + ".", filename[:-4])
        n += 1

    charName = input("\nChoose your character (name): ")

    # If user does not exist or mistype
    '''
    for filename in os.listdir(savesDir):
        if(charName != filename[:-4]):
            print("Error: Username does not exist. Please try again.")
            exit()
    '''
    
    player = pickle.load(open(savesDir + "/" + charName + ".pkl", "rb")) # Saved char file
    return(player)


def move(curPos, x, y, worldSize):
    # Direction in which user chooses
    print("\n------------------------------")
    dir = input("[Enter direction (n, e, s, w)]: ")

    # North
    if(dir is 'n'):
        outOfBounds = checkBounds(x - 1, y, worldSize)

        if(outOfBounds):
            print("\n------------------------------")
            print("***Out of bounds!***")
            print("------------------------------\n")
            return(curPos, x, y)

        else:
            print("\n------------------------------")
            print("You go North.")
            curPos = Layout.world1[x - 1][y]
            x = x - 1

    # East
    elif(dir is 'e'):
        outOfBounds = checkBounds(x, y + 1, worldSize)

        if(outOfBounds):
            print("\n------------------------------")
            print("***Out of bounds!***")
            print("------------------------------\n")
            return(curPos, x, y)

        else:
            print("\n------------------------------")
            print("You go East.")
            curPos = Layout.world1[x][y + 1]
            y = y + 1

    # South
    elif(dir is 's'):
        outOfBounds = checkBounds(x + 1, y, worldSize)

        if (outOfBounds):
            print("\n------------------------------")
            print("***Out of bounds!***")
            print("------------------------------\n")
            return(curPos, x, y)

        else:
            print("\n------------------------------")
            print("You go South.")
            curPos = Layout.world1[x + 1][y]
            x = x + 1

    # West
    elif(dir is 'w'):
        outOfBounds = checkBounds(x, y - 1, worldSize)

        if (outOfBounds):
            print("\n------------------------------")
            print("***Out of bounds!***")
            print("------------------------------\n")
            return(curPos, x, y)

        else:
            print("\n------------------------------")
            print("You go West.")
            curPos = Layout.world1[x][y - 1]
            y = y - 1

    # Direction not allowed
    else:
        print("\nThat is not a direction.\n")
        return(curPos, x, y)

    return(curPos, x, y)


def checkBounds(x, y, worldSize):
    # Check if user is out of bounds in world
    if(x > worldSize[1] or x < worldSize[0] or y > worldSize[1] or y < worldSize[0]):
        return(1)


def printWorld(world, x, y):
    # Erase previous move
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == 'o':
                world[i][j] = '-'
            else:
                continue

    # Print/show world to user
    curPosIcon = 'o'
    world[x][y] = curPosIcon
    print("")
    print('\n'.join(''.join(str(i).center(5) for i in row) for row in world))
