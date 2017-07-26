def backdoor():
    print("You are at the back door to the office.")
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

        choice = int(input("> "))

        if choice == 1:
            lobby_room()
        
        elif choice == 2:
            print("Nothing happens.")

        elif choice == 3:
            print("You see a filthy envelope on the ground.")
            print("Do you pick it up? (yes/no)")
            choice = input("> ")
            if choice == "yes":
                print("You pick up the envelope. A centipede crawls onto your hand.")
                has_envelope = True
                backdoor()
            else:
                print("You're right - too gross!")

        else:
            print("Oh well, come back again if you want.")
            exit(0)
