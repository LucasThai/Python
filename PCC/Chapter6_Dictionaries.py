'''
alien = {"color": "green", "point": 5}
new_points = alien["point"]
color = alien["color"]
print(f"You just earned {new_points} points!")
print(f"U R {color}")
'''

# adding new key value pairs
'''
alien = {"color": "green", "point": 5}
print(alien)

alien['x_pos'] = 0
alien['y_pos'] = 25
print(alien)
'''

# start w mt dictionary
'''
alien = {}
alien['color'] = 'green'
alien['points'] = 706
print(alien)
'''

# modifying values
'''
alien = {}
alien['color'] = 'green'
alien['points'] = 706
print(f"the alien is {alien['color']}.")

alien['color'] = 'black'
print(f"the alien like niggas so he's now {alien['color']}")
'''
# more interesting eg of modifying values
'''
alien_pos = {'x_pos': 0, 'y_pos': 0, 'z_pos': 0}

if keyboard.is_pressed('w'):
    alien_pos['x_pos'] = 5
elif keyboard.is_pressed('a'):
    alien_pos['y_pos'] = -5
elif keyboard.is_pressed('s'):
    alien_pos['x_pos'] = -5
elif keyboard.is_pressed('d'):
    alien_pos['y_pos'] = 5
print(alien_pos)
not working
'''

# removing key value pairs
'''
alien = {}
alien['color'] = 'green'
alien['points'] = 706
print(f"the alien is {alien['color']}.")

alien['color'] = 'black'
print(f"the alien like niggas so he's now {alien['color']}")

del alien['color']
print(f"deleted skin color of alien {alien}")
'''

# dict of similar objs
'''
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'lucas': 'trinh ha'
}
lang = fav_lang['lucas'].title()
print(f"lucas's fav language is {lang}")
'''

# 6-1
'''
Cong_info = {'first_name': 'Hong Cong',
             'last_name': 'Thai',
             "DOB": '10/10/1963'}
Trinh_info = {'first_name': 'Ha Trinh',
              'last_name': "Le",
              "DOB": '07/06/2007'}

print(Cong_info['DOB'], Trinh_info['first_name'])
'''
# 6-2
'''
fav_numbers = {'Cun': 7,
               'Trinh': 1,
               'Van Anh': 8,
               'Cong': 8}
print(fav_numbers['Cun'])
'''

# 6-3
'''
glossary = {'print': 'printing result into console',
            '.title()': 'making the word to have capital letters',
            '.upper()': 'fully capital',
            '.lower()': 'fully lower',
            'list[]': 'list is creating a list of strings'}
for word, meaning in glossary.items():
    print(f"{word}:\n   {meaning} \n")
print(glossary.items)
'''

# looping thru a dict
'''
user_0 = {
    'username': 'thaianhquan',
    'first name': 'Anh Quan',
    'last name': 'Thai',
    'DOB': '13/02/2007'
}
for key, value in user_0.items():
    print(f"\n key: {key}")
    print(f"Value: {value}")
'''

'''
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'lucas': 'trinh ha'
}

friends = ['lucas', "edward"]
for k, v in fav_lang.items():
    if k in friends:
        print(f"\nHi {k.title()}, I C U love {v.title()}")
    else:
        print(f"\nHi {k.title()}, please pick the poll ")
'''
# => these r the ways
'''

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'lucas': 'trinh ha',
    'anne': 'c#',
    'ben': 'react',
    'cameron': "c++"
}
for name in fav_lang: 
    print(name.title())
for name in fav_lang.keys(): #same as above
    print(name.title())
for k, v in fav_lang.items(): #loop key and value
    print(f"\nHi {k.title()}, I C U love {v.title()}")
'''
# looping thru dict 's key in an order using sorted(list)
'''
for name in sorted(fav_lang.keys()): #loop thru rearranged key and value
    print(f"{name.title()}, thank you for taking the poll")
'''
# looping thru all values
'''
print("the mentioned langs are")
for language in fav_lang.values():
    print(language.title())
'''

# Section: using get() to access value
'''
alien = {"skin": "green",
         "speed": "slow"}


point_value = alien.get("points", "no point value assigned.")
#if its being called and no value -> the second double quotation mark

print(point_value)
'''

# wrap dict in set() to avoid repetitive list
'''
for lang in set(fav_lang.values()):
    print(lang)
'''
# 6-4:
'''
glossary = {'print': 'printing result into console',
            '.title()': 'making the word to have capital letters',
            '.upper()': 'fully capital',
            '.lower()': 'fully lower',
            'list[]': 'list is creating a list of strings'}
for word, meaning in glossary.items():
    print(f"{word}:\n   {meaning} \n")
'''
# 6-5
'''
pop_river = [
    {
        "Nile": "Egypt",
        "Amazon": "Brazil",
        "Yangtze": "China",
        "Mississippi": "US",
    },
    {
        "1": "Nile go thru Egypt",
        "2": "Amazon go thru Brazil",
        "3": "Yangtze go thru China",
        "4": "Mississippi go thru US"
    }
]
for k, v in pop_river[0].items():
    print(f"The {k.title()} is in {v.title()}")
for v in pop_river[1].values():
    print(v)

'''
# 6-6
'''
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'lucas': 'trinh ha',
    'anne': 'c#',
    'ben': 'react',
    'cameron': "c++"
}
poll = ['jen', 'sarah', 'lucas', 'ben', 'quan']
for k, v in fav_lang.items():
    if k in poll:
        print(f"thanks {k.title()}, for taking our poll")
    else:
        print(f"Please take the poll, {k.title()}")
'''


# NESTING

# A list of dicts
# e.g list in dicts
'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
'''

# E.g 2:
'''
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'low'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[5:8]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:9]:
    print(alien)
'''

# A list in a dict not list of dicts
'''

pizza = {'crust': ['thin', 'thick'],
         'toppings': ['mushrooms', 'extra cheese', 'extra pepperoni']}

print(
    f'You ordered a {', '.join(pizza["crust"])} - crust pizza with {', '.join(pizza["toppings"])} on top')
'''

'''
fav_langs = {
    'Jen': ['Python,Ruby'],
    'Sarah': ['C'],
    'Phil': ['Python', 'Haskell'],
    'Edward': ['Ruby', 'Go']
}
for k, v in fav_langs.items():
    print(f"{k}'s favorite languages are: \n \t {', '.join(v)}\n")
'''


# A DICT IN A DICT
'''
users = {
    'thaianhquan': {
        'first': 'Anh Quan',
        'last': 'Thai',
        'location': 'Viet Nam'
    },
    'hatrinh2007': {
        'first': 'Ha Trinh',
        'last': 'Le',
        'location': 'Viet Nam'
    },
    'Hongcong1963': {
        'first': 'Hong Cong',
        'last': 'Thai',
        'location': 'Russia'
    }
}

for k, v in users.items():
    print(f"\nusername: {k}")
    print(f'full name: {v['first']} {v['last']}')
    print(f'Location: {v['location']}')
'''


# 6-7
'''
Cong_info = {'first_name': 'Hong Cong',
             'last_name': 'Thai',
             "DOB": '10/10/1963'}
Trinh_info = {'first_name': 'Ha Trinh',
              'last_name': "Le",
              "DOB": '07/06/2007'}
Quan_info = {'first_name': 'Anh Quan',
             'last_name': 'Thai', 'DOB': '13/02/2007'}

print(
    f'full name: {Cong_info['first_name']} {Cong_info["last_name"]}\nDOB: {Cong_info["DOB"]}')
print(
    f'full name: {Trinh_info['first_name']} {Trinh_info["last_name"]}\nDOB: {Trinh_info["DOB"]}')
print(
    f'full name: {Quan_info['first_name']} {Quan_info["last_name"]}\nDOB: {Quan_info["DOB"]}')
'''

# 6-10
'''
fav_num = {
    'Lucas': 7,
    'Emma': 6,
    'Tony': 1,
    'Linda': 2
}
for k, v in fav_num.items():
    print(f"{k}'s fav number is {v}")

'''


# 6-11
'''
Cities = {
    'Ha Long Bay': {
        'Country': 'Viet Nam',
        'Population': 'approx 300,000',
        'Fact': 'UNESCO world heritage site'
    },
    'Paris': {
        'Country': 'France',
        'Population': 'approx 2.1 million',
        'Fact': 'Home to Eiffel Tower'
    },
    'NYC': {
        'Country': 'United States',
        'Population': 'approx 8.5 million',
        'Fact': 'The most linguistically city in the world'
    }
}

for k, v in Cities.items():
    print(
        f"{k}'s city is located in {v['Country']}, with a population {v['Population']}, and a fact for this city is {v['Fact']}\n")
'''
