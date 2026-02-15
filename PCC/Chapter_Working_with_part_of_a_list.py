# Working_with_part_of_a_list
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])
print(players[-3:])
print(players[:4])
'''

# looping through a slice
'''players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player, end=" ")
'''

# copying a list
'''my_food = ['broccoli', 'beef', 'eggs', 'lean beef']
your_food = my_food[:]

my_food.append("chicken thigh")
your_food.append("shit")
print("My fav food are: ", my_food)
print("Your food are: ", your_food)
'''

# 4-10
'''my_food = ['broccoli', 'beef', 'eggs', 'lean beef']
print("The first three items in the list are:")
for food in my_food[:3]:
    print(food)
print("Three items from the middle of the list are:")
for foods in my_food[1:3]:
    print(foods)
print("The last three items in the list are:")
for fud in my_food[1:]:
    print(fud)

'''
# 4-11
'''Pizzas = ["pepperoni", "Neapolitan", "Cheese", "BBQ chicken",
          "Hawaiian", "Buffalo chiken", "Meat lover"]
friend_pizza = Pizzas[:]
Pizzas.append("cock")
friend_pizza.append("pzzzy")
print("These are my pizzas")
for pizza in Pizzas:
    print(pizza)
print("\nThese are your pizzas")
for pizzas in friend_pizza:
    print(pizzas)
'''

# 4-12
'''my_food = ['broccoli', 'beef', 'eggs', 'lean beef']
your_food = my_food[:]
my_food.append("chicken thigh")
your_food.append("shit")
print("\nMy food are: ")
for food in my_food:
    print(food)
print("\nYour food are: ")
for frfud in your_food:
    print(frfud)
'''
