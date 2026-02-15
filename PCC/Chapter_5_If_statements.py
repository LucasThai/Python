'''
cars = ["audi", "Lexus", "Mercedes", "Toyota", "Subaru"]
for car in cars:
    if car == "audi":
        print(car.upper())
    else:
        print(car.title())
'''
'''
Passwords = []
Passwords = input("Please set your password: ")
EnterPass = []
EnterPass = input("Please enter your password: ")
if EnterPass != Passwords:
    print("Access Granted")
else:
    print("Acess Denied")
'''
'''
passwords = []
passwords = input("Please enter your password: ")
total_chars = len(passwords)
checker = 0
if total_chars < 6:
    print("Password is very weak")
    passwords = input("Please set a longer password: ")
elif total_chars <= 8:
    print("Password is weak")
    passwords = input("Please set a longer password: ")
elif total_chars <= 10:
    print("Password is Medium")
    passwords = input("Please set a longer password: ")
else:
    print("Password is strong")
'''

# 5-1
'''
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
'''
'''
Car = ["Lexsus", "Audi"]
Guessin = []
Guessin = input("Please enter a car brand: ")
if Guessin in Car:
    print("Found: ", Guessin)
else:
    print("Not found: ", Guessin)
'''

# 5-3 & 5-4
'''
alien_color = ["green", "yellow", "red"]
guessin = []
guessin = input("Guess what color is the alien? \n")
if guessin in alien_color[0]:
    print("You have earned 5 points")
elif guessin in alien_color[1]:
    print("You earned 10 points")
elif guessin in alien_color[2]:
    print("You earned 15 points")
else:
    print("Nope!")
'''
# 5-6
'''
ages = [2, 4, 3, 7, 14, 32, 82]

for age in ages:
    if age < 2:
        print("This is a baby")
    elif age < 4:
        print("This is a toddler")
    elif age < 13:
        print("This person is a kid")
    elif age < 20:
        print("This person is a teenager")
    elif age < 65:
        print("This person is an adult")
    else:
        print("This person is an elder")
'''
'''
# 5-7
favf = ["Pineapple", "Apple", "Mango", "Banana", "Blueberry"]
Guessin = []
Guessin = input("Please guess \n")
if Guessin in favf:
    print(f"{Guessin} is correct")
else:
    print(f"{Guessin} is not correct")
'''

# Checking for special items
'''
requested_toppings = []
print("What toppings do you like? \n mushrooms? green peppers? extra cheese?")
while True:
    requested_toppings = input("Please add toppings: \n")
    if requested_toppings == "mushrooms":
        print("Added mushroom")
    elif requested_toppings == "green peppers":
        print("Sorry, We are out of peppers")
    elif requested_toppings == "extra cheese":
        print("Added cheese")
    elif requested_toppings == "cancel":
        print("Order")
        break
    else:
        print("We don't have that kind of topping")
'''

# Using multiple lists
available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = []
print("These are our available toppings: \n blah blah blah")
while True:
    requested_toppings = input(
        "What toppings would you like for your pizza? \n")
    if requested_toppings in available_toppings:
        print(f"adding {requested_toppings}")
    elif requested_toppings == "cancel":
        print("That's all?")
        break
    else:
        print(f"{requested_toppings} is not available")
