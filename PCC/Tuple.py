'''
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
'''

# 4-13
menu = ("beef", "chicken ",
        "chicken breast", "lamb", "pussy")
for food in menu:
    print(food)

menu = ("beef", "chicken ",
        "titties", "cock", "pussy")
print("\n modified menu")
for food in menu:
    print(food)

# tuples are immutable, so their
# contents can't be changed accidentally — good for fixed data and for reasoning about code.
