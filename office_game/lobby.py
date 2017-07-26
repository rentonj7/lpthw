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
        print(f"You say {choice}.  Marika tells you that the basement is flooded.")
#        lobby_room()

    elif choice == 2:
        print("You see a broken stapler on the desk.")

    else:
        print("That wasn't an option")
