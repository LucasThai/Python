# Defining a function
'''
def greet_user():
    print("Hello")


greet_user()
'''

# passin info to a function
'''
def greet_user(username):
    print(f"Hello, {username.title()}!")


greet_user("lucas")
'''

# 8-1
'''
def display_message():


    print("This chapter I am learning how to do function in python:")
display_message()
'''

# 8-2
'''
def fav_bok(title):
    print(f"one of my fav book is {title}")


fav_bok('alice in wonder land')
'''

# Positional arguments
'''
def describe_pet(pet_type, pet_name):
    print(f"I got a {pet_type} called {pet_name}")


describe_pet('dawg', 'Pitbull')
describe_pet('dawg', 'Chihuahua')
'''

#8-3
'''
def make_shirt(size, txt_on_shirt):
    print(f"Your order is a {size} sized shirt with {txt_on_shirt} on the front")


size = input("What size for the shirt? (S/M/L/XL)\n")
txt_on_shirt = input("What text would u like on the shirt?\n")
make_shirt(size, txt_on_shirt) 
'''

# 8-4
'''
def make_shirt(size="Large", txt_on_shirt="I love Python"):
    print(
        f"Your order is a {size} sized shirt with {txt_on_shirt} on the front")


size = input("What size for the shirt? (S/M/L/XL)\n")

txt_on_shirt = input("What text would u like on the shirt?\n")

make_shirt(size, txt_on_shirt)
'''


# RETURNING A SIMPLE VALUE & making an argument OPTIONAL
'''
def get_formatted_name(f_name, last_name, mid_name=''):
    if mid_name:
        full_nam = f"{f_name} {mid_name} {last_name}"
    else:
        full_nam = f"{f_name} {last_name}"
    # return full_nam.title()
    print(full_nam)


get_formatted_name("Quan", "Thai", "Anh")

get_formatted_name("Ha Trinh", "Le")

# Difference between these two code blocks is above return none,
# below returns the formatted name so we can store and use it so below is much flexible


def get_formatted_name(f_name, last_name, mid_name=''):
    if mid_name:
        full_nam = f"{f_name} {mid_name} {last_name}"
    else:
        full_nam = f"{f_name} {last_name}"
    return full_nam.title()


musician = get_formatted_name("Quan", "Thai", "Anh")
print(musician)
musician1 = get_formatted_name("Ha Trinh", "Le")
print(musician1) 
'''

# Using a function with a while loop


# 8-6
# 8-7
'''
def make_album(art_name, alb_title, num_of_sogs=None):
    Album = {
        "Artist name": art_name,
        "album title": alb_title,
    }
    if num_of_sogs:
        Album['Number of songs'] = num_of_sogs
    return Album


while True:
    art_nam = input("\nplease input your artist name: ")
    alb_tit = input("And the title of the album: ")
    num_of_sos = input("Number of songs: (press Q to skip)\n")
    if num_of_sos in ('q', 'Q'):
        print(make_album(art_nam, alb_tit))
        break
    else:
        print(make_album(art_nam, alb_tit, num_of_sos))
        break
'''

# PASSING A LIST
# 8-9 & 8-10

'''
def show_mesage(tex_mess, sent_mess):
    print(f"Here are the original messages: \n {',  '.join(tex_mess)}")
    while tex_mess:
        s = tex_mess.pop()
        print(f"Sending messages: {s}")
        sent_mess.append(s)


def show_sent_mess(sent_mess):
    print('\n the following messages has been sent: ')
    for sent in sent_mess:
        print(sent)


tex_mess = ['trinh', 'quan', 'cong', 'van']
sent_mess = []
show_mesage(tex_mess, sent_mess)
show_sent_mess(sent_mess)
'''


# PASSIN An arbitrary nber of arguments
'''
def make_piz(size, *toppings):
    print(f"\n Making {size} sized pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_piz(16, 'Pepperoni')
make_piz(10, 'Mushrooms', 'Green peppers', 'Extra cheese')
'''
# *toppings tells python to create a tuple called toppings (toppings = ())

'''
def build_prof(first, last, **user_info):
    user_info['First name'] = first
    user_info['Last name'] = last
    return user_info


user_prof = build_prof('Anh Quan', 'Thai', location='Ha Long',
                       field='Electrical Engineering', Subfield='ML engineer')
print(user_prof) 
'''
# **user_info tells py to create a dict called user_info
#  (user_info = {'first name' = first,
#                 'last name' = last,
#                 'location' = 'Ha Long',
#                 'Any_user_info values' = 'user_info data'})


# 8-12
'''
def make_sandwichz(*toppings):
    print('\n making sandwich with the following toppings: ')
    for topping in toppings:
        print(f'- {topping}')


make_sandwichz('ham', 'cheese', 'tomatoes')
make_sandwichz('shid', 'puzzy', 'trinhs pussy water')
make_sandwichz('tomatoes') 
'''


# 8-13 finished
# 8-14
'''
def car_info(manuf, model_name, **car_features):
    car_features['Manufacturer'] = manuf
    car_features['Model name'] = model_name
    return car_features


car = car_info('Subaru', 'Outback', color='blue', tow_package=True)
print(car)
'''

# STORING YOUR FUNCTIONS IN MODULE

# pizza.py got the function make_pizza, proceed to create another making_pizza.py (pretend this is it)
'''
def make_piz(size, *toppings):
    print(f"\n Making {size} sized pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
'''

# Import entire module
'''
import pizza

pizza.make_pizza(16,'pepperoni', 'Extra cheese')
'''
# Using as to give module an alias
'''
import pizza as p

p.make_pizza(20, ...)
'''
# Import specific function
'''
from pizza import make_pizza

make_pizza(12, 'Extra cheese')
'''
# Using as to give alias
'''
from pizza import make_pizzas as mp

mp.make_pizza(8, ...)
'''

# Import all functions in a module
'''
from pizza import *

make_pizza(12,...)
'''

 
