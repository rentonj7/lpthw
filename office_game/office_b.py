from sys import exit

def backdoor():
    print("You are at the back door to the office.")
    print("Is the business open?")

    bus_open = input("> ")

    if bus_open == "yes":
        print(f"You said {bus_open}, what do you want to do?")
        choice = input("> ")

        if choice == "open door" or "go in":
            lobby_room()

        else:
            print("Oh well, come back again if you want.")
            exit(0)


def lobby_room():
    print("You are in the lobby.")
    print("""
    Marika is at the desk. Do you:
        1)  Say "Hi"
        2)  Look around
        3)  Walk into the conference room
        4)  Walk to the kitchen

        (enter the number of your choice)
        """)
    choice = input("> ")

    if choice == 1:
        print(f"You say {choice}.  Marika tells you that the basement is flooded."
        lobby_room()

    elif choice == 2:
        print("You see a broken stapler on the desk.")



def start():
    backdoor()

#def enter_number():
#    current_choice = int(input("> ")

# This calls the start function to start the game!
backdoor()
