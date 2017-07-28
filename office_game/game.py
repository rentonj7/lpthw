from sys import exit

#  These are the variables to determine dialogue

# Lobby variables
bus_open = "no"

prompt = "> "
number_prompt = "Please enter the # of your choice: "

# This is the inventory list.  It starts out empty.

inventory = []

def inventory_lister():
    if inventory != []:
        for i in inventory:
            print("In your inventory: " + i) 
            print("\n")
    else:
        print("Your inventory is empty.\n")

# The backdoor scene
def backdoor():
    global bus_open

    print("You are at the back door to the office.")
    
    while bus_open != "yes":
        print("Is the business open?")

        bus_open = input("> ")

    if bus_open == "yes":
        print("""
        Great, it's open.  Now what?

        1) Open door
        2) Knock on door and run away
        3) Look around
        4) Leave
        """)
        inventory_lister()

        choice = int(input(number_prompt))

        if choice == 1:
            print("You open the back door and head inside . . .")
            lobby_room()
        
        elif choice == 2:
            print("Nothing happens.")
            backdoor()

        elif choice == 3:
            print("You see a filthy envelope on the ground.")
            print("Do you pick it up? (yes/no)")
            choice = input(prompt)
            if choice == "yes":
                print("You pick up the envelope. A centipede crawls onto your hand.\n")
                inventory.append('envelope')
                backdoor()
            else:
                print("You're right - too gross!\n")
                backdoor()

        else:
            print("Oh well, come back again if you want.")
            exit(0)

# The lobby scene
def lobby_room():
    print("You are in the lobby.")
    print("""
Marika is at the desk. Do you:

1)  Say "Hi"
2)  Look around
3)  Walk into the conference room
4)  Walk to the kitchen """)
    
    if "envelope" in inventory:
        print("5)  Give Envelope to Marika?")

    print("enter the number of your choice")
    inventory_lister()

    choice = int(input(number_prompt))

    if choice == 1:
        print(f"You say {choice}.  Marika tells you that the basement is flooded.")
        lobby_room()

    elif choice == 2:
        print("You see a broken stapler on the desk.")

    else:
        print("That wasn't an option")


def start():
    backdoor()
    
start()
