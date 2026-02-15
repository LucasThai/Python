'''
age = int(input("How old are you? \n"))
if age >= 18:
    print("You are qualified for watching film")
else:
    print(f"Because you are {age}, you can't watch film yet")
'''

# THE MODULO OPERATOR %
# print(3 % 2, 4 % 3, 5 % 3, 3 % 3, 3 % 6,)


# Even or odd
'''
num = int(input("Type a number, and I'll tell you if it's even or odd \n"))
if num % 2 == 0:
    print(f"This number {num} is even")
else:
    print(f"This number {num} is odd")
'''

# 7-3
'''
num = int(input(
    "Type a number, and I'll tell you whether the number is a multiple of 10 or not\n"))
if num % 10 == 0:
    print(f"{num} is a number multiple of 10")
else:
    print(f"{num} is not multiple of 10")
'''


# INTRODUCE WHILE LOOPS
'''
x = 1
while x <= 5:
    print(x)
    x += 1
'''


# 7-4
'''
Toppings = []
while True:
    prt = input(
        "Please enter toppings of your choice (type 'quit' to quit the program')\n")
    if prt == 'quit':
        print(f"\nYour choices for pizza toppings are: {", ".join(Toppings)}")
        break
    else:
        Toppings.append(prt)
        print(f"added {prt}. \n")
'''


# 7-5
'''
prmpt = int(input("Before purchasing, How old are you?\n"))
if prmpt < 3:
    print("Ticket is free")
elif prmpt < 12:
    print("Ticket is 10$")
else:
    print("Ticket is 15$")
'''


# 7-6
'''
num_tick = int(input("How many tickets are you buying? \n"))
x = 0
age_eachtick = []
while x != num_tick:
    prmpt = input("How old is the person's ticket?\n")
    x += 1
    if prmpt == 'quit':
        break
    prmpt = int(prmpt)
    if prmpt < 3:
        print("Ticket is free")
        age_eachtick.append('free')
    elif prmpt < 12:
        print("Ticket is 10$")
        age_eachtick.append('10$')
    else:
        print("Ticket is 15$")
        age_eachtick.append('15$')
print(f"Price for each ticket are: {', '.join(age_eachtick)}")
'''

# 7-7 infinity
'''
while True:
    print('iluvT')
'''


# Moving items from one list to another
# check out if a person has been checked by doctor
'''
unchecked_users = []
checked_users = []
while True:
    action = input(
        "What do you want to do? (check in / check out / list / quit)\n"
    ).strip().lower()

    if action in ("check in", "in", "checkin"):
        users_name = input("What is your full name?\n").strip().title()
        unchecked_users.append(users_name)
        print(f"Waiting for doctor: {', '.join(unchecked_users) or 'none'}")

    elif action in ("check out", "out", "checkout"):
        name = input("What is your full name?\n").strip().title()
        if name in unchecked_users:
            unchecked_users.remove(name)
            checked_users.append(name)
            print("Thank you, you are finished for checking out")
        else:
            print("Name not found in check-in list; please check in first")
        print(f"Checked out users: {', '.join(checked_users) or 'none'}")

    elif action in ("list", "show", "status"):
        print(f"Waiting for doctor: {', '.join(unchecked_users) or 'none'}")
        print(f"Checked out users: {', '.join(checked_users) or 'none'}")

    elif action in ("quit", "exit"):
        print("Goodbye!")
        break

    else:
        print("Please answer with: check in / check out / list / quit")
'''


# 7-8
'''
sandwich_orders = ['Tortas', 'Panini',
                   'Grilled cheese', 
                   'Pastrami', 'Blt sandwich', 
                   'Pastrami', 'Banh Mi', 
                   'Pastrami']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made you your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print(
    f"All the sandwiches has been made: {', '.join(finished_sandwiches)}")
'''

# 7-9
'''
import time
sandwich_orders = []
finished_sandwiches = []

available = [
    "tortas",
    "panini",
    "grilled cheese",
    "blt sandwich",
    "banh mi"
]

while True:
    Menu = input(
        "Would you like to Order our sandwiches? (Yes/No/Cart/Finished)\n").strip().lower()
    if Menu in ('Yes', 'yes', 'Y', 'y'):
        while True:
            orders = input(
                "We have these sandwiches: \n \t Tortas, Panini, Grilled cheese, Pastrami, Blt sandwich, Banh Mi\n What would you like for today? (Type one by one)\n").strip().lower()
            if orders in ('back', 'b'):
                break
            elif orders in available:
                print(f"\n added {orders}")
                sandwich_orders.append(orders)
            elif orders == 'pastrami':
                print("Sorry, we are out of stock")
            else:
                print('sorry, that item is not in our available menu\n')
    elif Menu in ('no', 'n'):
        break
    elif Menu in ('cart', 'c'):
        print(f"These are your orders: {', '.join(sandwich_orders)}")
    elif Menu in ('finished', 'f'):
        print(f"These are your orders: {', '.join(sandwich_orders)}")
        print("Thank you for ordering our sandwiches, now we are cooking it")
        time.sleep(3)
        while sandwich_orders:
            processing = sandwich_orders.pop(0)
            finished_sandwiches.append(processing)
        print(
            f"Your orders: {', '.join(finished_sandwiches)} has been cooked.")
        break

    else:
        print("Sorry, we only have Yes/No/Cart/Finished")
        continue
'''
# 7-10 dict
active_poll = True
responses = {}
while active_poll:
    name = input("what's ur name?\n").strip().title()
    dr_vaca = input("where is ur dream vacation? \n")
    responses[name] = dr_vaca
    pollstatus = input(
        "Is there anyone taking poll after you?").strip().lower()
    if pollstatus == 'yes':
        continue
    elif pollstatus == 'check responses':
        print(responses)
    else:
        break
