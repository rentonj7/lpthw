print("How are you today?")
print("""
1. Good
2. Bad
3. In between
""")

feeling = input("> ")

if feeling == "1":
    print("I'm glad you're feeling good today.  What's got you so up?")
    good_feeling = input("> ")
    print(f"I'm glad for you that your day included {good_feeling}")

elif feeling == "2":
    print("Too bad, so sad.")

else:
    print("Can't make up your mind?")
