# for looping
'''cars = ['porsch', 'bmw', 'lexus', 'merc', 'toyota', 'subaru']
for car in cars:
    print(car)

# work with for loop
for car in cars:
    print(f"{car.title()}, that is a exotic brand")
    print(f"i cant wait to get this car, {car.title()} \n")
print("thank you for having me here")
'''

# 4-1: pizzas
'''Pizzas = ["pepperoni", "Neapolitan", "Cheese", "BBQ chicken",
          "Hawaiian", "Buffalo chiken", "Meat lover"]
for pizza in Pizzas:
    print(pizza)
print("I really love pizza")
'''

# 4-2
'''Animals = ["Dog", "cat", "cock", "girrafe", "elephant"]
for animal in Animals:
    print(f"this {animal} would be a great pet")'''


# Making numerical lists

# using the range() function
'''for value in range(1, 100):
    print(value)'''

# using range() to make a list of number
'''numbers = list(range(1, 51))
print(numbers)'''

'''even_numbers = list(range(2, 20, 2))
odd_numbers = list(range(1, 20, 2))
print(even_numbers)
print(odd_numbers)'''


'''squared_numbers = []
for value in range(1, 20, 1):
    num = value ** 2
    squared_numbers.append(num)
print(squared_numbers)'''

'''for value in range(1, 11):
    squared_numbers.append(value**2)
print(squared_numbers)
'''

# simple statistics with a list of numbers
'''digits = [13, 0, 2, 2, 7, 6, 8, 9, 11, 21]
print(sum(digits))
'''

# list comprehensions
'''squared_numbers = [value+2 for value in range(1, 20)]
print(squared_numbers)
'''

# 4-3
'''for value in range(1, 21):
    print(value, end=" ")
'''
# 4-4 & 4-5
'''numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
'''

# 4-6
'''odd_numbers = list(range(1, 21, 2))
print(odd_numbers)
'''

# 4-7
'''multi3 = list(range(0, 30, 3))
print(multi3)
'''

# 4-8 & 4-9
'''cubes = [value**3 for value in range(1, 11)]
print(cubes)
'''
