# Main Menu file for the text-based game
# Author: John L Garcia

import Defaults, MasterControl, SpaceSauce
import pickle, os


def main():
    # Title screen
    print("\n*** Main Menu ***")
    print("\n--- Space Sauce ---\n")
    print("Options:")
    print("1. Create new character")
    print("2. Load character")

    option = int(input("Select option: "))

    if(option == 1):
        createNewCharacter()
    elif(option == 2):
        loadCharacter()
    else:
        print("\nThat is not an option. Please choose an option from above.")


def createNewCharacter():
    # Create a class
    print("\n---Classes---")

    # Class 1 - Assault
    print("\n1. -Assault-")
    print("Description: A well-balanced soldier. Handles medium-long encounters well.")
    print("Weapon: Assault Rifle")
    print("-Stats-")
    print("Accuracy:", Defaults.defaultStats["Assault"]["Accuracy"])
    print("Intelligence:", Defaults.defaultStats["Assault"]["Intelligence"])
    print("Agility:", Defaults.defaultStats["Assault"]["Agility"])

    # Class 2 - Engineer
    print("\n2. -Engineer-")
    print("Description: A smart fellow who knows his/her tools. Handles close-medium encounters well.")
    print("Weapon: Sub Machine Gun")
    print("-Stats-")
    print("Accuracy:", Defaults.defaultStats["Engineer"]["Accuracy"])
    print("Intelligence:", Defaults.defaultStats["Engineer"]["Intelligence"])
    print("Agility:", Defaults.defaultStats["Engineer"]["Agility"])

    # Class 3 - Support
    print("\n3. -Support-")
    print("Description: A useful fellow who understands his/her equipment. Handles close encounters well.")
    print("Weapon: Shotgun")
    print("-Stats-")
    print("Accuracy:", Defaults.defaultStats["Support"]["Accuracy"])
    print("Intelligence:", Defaults.defaultStats["Support"]["Intelligence"])
    print("Agility:", Defaults.defaultStats["Support"]["Agility"])

    # User selects class
    charClass = int(input("\nSelect your class (number): "))

    # Assault class
    if(charClass == 1):
        print("\nYou selected the Assault class.")
        className = "Assault"
        classStats = Defaults.defaultStats["Assault"] # Get class stats from DefaultClasses.py
        classGun = "Assault Rifle"
        classGunDamage = Defaults.gunDamage["Assault Rifle"]

    # Engineer class
    elif(charClass == 2):
        print("\nYou selected the Engineer class")
        className = "Engineer"
        classStats = Defaults.defaultStats["Engineer"]
        classGun = "Sub Machine Gun"
        classGunDamage = Defaults.gunDamage["Sub Machine Gun"]

    # Recon class
    elif(charClass == 3):
        print("\nYou selected the Support class")
        className = "Support"
        classStats = Defaults.defaultStats["Support"]
        classGun = "Shotgun"
        classGunDamage = Defaults.gunDamage["Shotgun"]

    # Class selection error
    else:
        print("\nThat class does not exist. Choose one of the provided classes.")

    # response = input("\nIs this correct? (y or n): ")

    # User chooses a name
    userName = input("\nEnter a name for your character: ")

    # reponse = input("\nIs this correct? (y or n): ")

    # Call to MasterControl to save created character
    MasterControl.save(userName, className, classGun, classGunDamage, classStats)

    curDir = os.path.realpath(os.path.dirname(__file__))                    # Current directory
    savesDir = os.path.join(curDir, "Saves")                                # Saves directory
    player = pickle.load(open(savesDir + "/" + userName + ".pkl", "rb"))    # Saved char file

    # Start the game!
    SpaceSauce.start(player)


def loadCharacter():
    print("\n---Saved Characters---\n")

    player = MasterControl.load()

    print("")
    print("-------------------------------------------------------------------------------")
    print("---Summary---")
    print("Name:", player["Name"])
    print("Class:", player["Class"])
    print("Gun:", player["Gun"])
    print("Gun Damage:", player["Gun Damage"])
    print("Stats:", player["Stats"])
    print("-------------------------------------------------------------------------------")

    # Start the game!
    SpaceSauce.start(player)


# Call to main
main()
