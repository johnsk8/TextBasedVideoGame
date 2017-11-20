# The Space Sauce game file
# Author: John L Garcia

import Layout, MasterControl


def start(player):
    # Beginning story of game
    print("\n---Space Sauce---")
    print("\nYou wake up on your space ship dazed and clouded in smoke.")
    print("Sparks and smoke surround you.")
    input("\n[Press Enter to continue...]\n")

    print("You're strapped to your seat and alive.")
    print("After you un-buckle, you slowly stand up to observe the rest of the ship.")
    print("No one else is aboard. Oh right. You travel alone remember.")
    input("\n[Press Enter to continue...]\n")

    print("You view the outside through a window now feeling more aware of your surroundings.")
    print("'What do I do?' you think. ")
    input("\n[Press Enter to continue...]\n")

    print("Your scanners indicate the atmosphere is safe to breathe.")
    print("Better grab your equipment to embark the outside.")
    input("\n[Press Enter to continue...]\n")

    print("Since you're a(n)", player["Class"], "class you know having a", player["Gun"] , "is the way to go.")
    input("\n[Press Enter to continue...]\n")

    print("As you exit, you notice there are 4 directions you could take: North (n), East (e), South (s), and West (w).")
    print("\nWhich direction will you take?")

    # The users current position in World 1
    x = 2 # x coord
    y = 2 # y coord
    curPos = Layout.world1[x][y]

    # Begin simulating World 1
    world1(curPos, x, y)


def world1(curPos, x, y):
    # Goal: Get the key and use that to open the gate
    key = 0

    # Show World 1 to user
    MasterControl.printWorld(Layout.world1, x, y)

    while(1):
        # Time to start moving
        curPos, x, y = MasterControl.move(curPos, x, y, Layout.world1_Size)
        print("Current position: (", x, "", y, ")")

        MasterControl.printWorld(Layout.world1, x, y)

        # User moves onto World 2 if he/she has key and is at the gate
        if(key == 1 and Layout.world1_Legend[x][y] == 'G'):
            print("You're going to World 2!")
            exit()

        # User moves around World 1 and encounters these scenarios
        if(Layout.world1_Legend[x][y] == 'S'):
            print("\nStarting point")
        elif(Layout.world1_Legend[x][y] == '-'):
            print("\nEmpty")
        elif(Layout.world1_Legend[x][y] == 'I'):
            print("\nItem")
        elif(Layout.world1_Legend[x][y] == 'M'):
            print("\nMonster")
        elif(Layout.world1_Legend[x][y] == 'G'):
            print("\nGate")
        elif(Layout.world1_Legend[x][y] == '*'):
            print("\nKey")
            key = 1
        else:
            print("You are lost my friend.")
