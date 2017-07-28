tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
multi_cat = "{}\\{}"

fat_cat = """
I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    """

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#these are my test strings

print("Gray cat \f goes around.")
print('''
        What is a cat
        That doesn't meow back?
        Who knows.
        ''')

print(multi_cat.format("Hi", "Bye"))
