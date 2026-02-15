# Intro: creatig a dog class
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_ov(self):
        print(f"{self.name} rolled over!")
'''
# The __init__() method at w is a special method that Python runs automatically whenever we create a new instance based on the Dog class.


'''print(f"Roof Roof, My dog is {Dog.name} and she's {Dog.age}")'''
# name and age are instance attributes and dog.name tries to access a class level attribute so only method below works
'''
my_dawg = Dog('Emma', 18)
ur_dawg = Dog("Lucas", 19)

print(f"My dog's name is {my_dawg.name} and she's {my_dawg.age}")
my_dawg.sit()
my_dawg.roll_ov()

print(f"\nMy dog's name is {ur_dawg.name} and he's {ur_dawg.age}")
ur_dawg.sit()
ur_dawg.roll_ov()
'''

# 9-1 & 9-2

'''
class restaurant:
    def __init__(self, res_name, cuisine_type):
        self.res_nam = res_name
        self.cuisine_type = cuisine_type

    def describe_rest(self):
        print(
            f"This restautrant called {self.res_nam}, mainly serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.res_nam} is now opening!!")


my_res = restaurant("Cún Trinh", "Vietnamese food")
my_res.describe_rest()
my_res.open_restaurant()

second_res = restaurant("Bún chả 96", "Grilled meat and rice vermicelli")
second_res.describe_rest()
second_res.open_restaurant()
'''

# 9-3
'''

class user:
    def __init__(self, first_n, last_n, location=None, Height=None):
        self.first_n = first_n
        self.last_n = last_n
        self.location = location
        self.Height = Height
        self.fullname = f"{self.first_n} {self.last_n}"

    def describe_user(self):
        print(f"Name: {self.fullname}")
        if self.location:
            print(f"- Location: {self.location}")
        if self.Height:
            print(f"- Height:{self.Height}")

    def greeting(self):
        print(f"Welcome {self.fullname} to the program!")


current_user = user('Anh Quan', 'Thai')
current_user.describe_user()
current_user.greeting()

print("\n")

user_dad = user('Hong Cong', 'Thai', 'Sydney, Australia', 168)
user_dad.describe_user()
user_dad.greeting()

print("\n")

user_wife = user('Ha Trinh', 'Le', 'Ha Long, Viet Nam', 165)
user_wife.describe_user()
user_wife.greeting()
'''


# WORKING WITH CLASSES AND INSTANCES

# The car class
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descrip_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model.upper()}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} Km on it")

    def update_odo(self, Kilom):
        if Kilom >= self.odometer_reading:
            self.odometer_reading = Kilom
        else:
            print("Nuh Uh")

    def incre_odo(self, Incre_km):
        self.odometer_reading += Incre_km


my_new_car = Car('Porsche', 'GT3 RS', 2025)
print(my_new_car.get_descrip_name())
# my_new_car.odometer_reading = 67

my_new_car.update_odo(0)
my_new_car.incre_odo(2)
my_new_car.read_odometer()
'''

# 9-4:
'''
class restaurant:
    def __init__(self, res_name, cuisine_type):
        self.res_nam = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_rest(self):
        print(
            f"This restautrant called {self.res_nam}, mainly serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.res_nam} is now opening!!")

    def set_number_served(self, number):
        self.number_served = number

    def incre_nber_served(self, incre_served):
        self.number_served += incre_served


my_res = restaurant("Cun & Trinh", "Vietnamese BBQ")

my_res.set_number_served(1)
my_res.incre_nber_served(2)
my_res.describe_rest()
my_res.open_restaurant()
print(f"\n {my_res.number_served}")
'''

# 9-5
'''
class User:
    def __init__(self, first_n, last_n, location=None, height=None):
        self.first_n = first_n
        self.last_n = last_n
        self.location = location
        self.height = height
        self.login_attempts = 0
        self.fullname = f"{self.first_n} {self.last_n}"

    def describe_user(self):
        print(f"Name: {self.fullname}")
        if self.location:
            print(f"- Location: {self.location}")
        if self.height:
            print(f"- Height:{self.height}")
        print(self.login_attempts)

    def greeting(self):
        print(f"Welcome {self.fullname} to the program!")

    def incre_login_attempts(self):
        self.login_attempts += 1

    def reset_log_attempts(self):
        self.login_attempts = 0


my_user = User('Anh Quan', 'Thai', 'Sydney, Australia', 176)
my_user.Incre_login_attempts()
my_user.reset_log_attempts()
my_user.Incre_login_attempts()
my_user.Incre_login_attempts()
my_user.describe_user()
'''


# INHERITANCE
# continue on class car
# Init method for Child class
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descrip_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model.upper()}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} Km on it")

    def update_odo(self, Kilom):
        if Kilom >= self.odometer_reading:
            self.odometer_reading = Kilom
        else:
            print("Nuh Uh")

    def incre_odo(self, Incre_km):
        self.odometer_reading += Incre_km

# child class


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} Km on full charge")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar("Porsche", "Taycan", "2025")
print(my_car.get_descrip_name())
my_car.battery.battery_size = 100
my_car.battery.describe_battery()
my_car.battery.get_range()
'''

# 9-6

'''
class IceCreamStand:
    def __init__(self, res_name, cuisine_type):
        self.res_nam = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.flavors = ["Chocolate", "Biscoff", "Strawberry"]

    def describe_rest(self):
        print(
            f"This restautrant called {self.res_nam}, mainly serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.res_nam} is now opening!!")

    def set_number_served(self, number):
        self.number_served = number

    def incre_nber_served(self, incre_served):
        self.number_served += incre_served

    def show_menu(self):
        print(f"These are the flavors for the ice cream:")
        for f in self.flavors:
            print(f"- {f}")


my_icekream = IceCreamStand("Cun & Trinh", "Ice cream cone")
my_icekream.describe_rest()
my_icekream.show_menu()
'''
'''

class Restaurant:
    def __init__(self, res_name, cuisine_type):
        self.res_nam = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_rest(self):
        print(
            f"This restautrant called {self.res_nam}, mainly serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.res_nam} is now opening!!")

    def set_number_served(self, number):
        self.number_served = number

    def incre_nber_served(self, incre_served):
        self.number_served += incre_served


class IceCreamStand(Restaurant):
    def __init__(self, res_name, cuisine_type):
        super().__init__(res_name, cuisine_type)
        self.flavors = ["Chocolate", "Biscoff", "Strawberry"]

    def show_menu(self):
        print(f"These are the flavors for the ice cream:")
        for f in self.flavors:
            print(f"- {f}")


my_icekream = IceCreamStand("Cun & Trinh", "Ice cream cone")
my_icekream.describe_rest()
my_icekream.show_menu()
'''

# 9-7
'''
class User:
    def __init__(self, first_n, last_n, location=None, Height=None):
        self.first_n = first_n
        self.last_n = last_n
        self.location = location
        self.Height = Height
        self.fullname = f"{self.first_n} {self.last_n}"

    def describe_user(self):
        print(f"Name: {self.fullname}")
        if self.location:
            print(f"- Location: {self.location}")
        if self.Height:
            print(f"- Height:{self.Height}")

    def greeting(self):
        print(f"Welcome {self.fullname} to the program!")


class Admin(User):
    def __init__(self, first_n, last_n, location=None, Height=None):
        super().__init__(first_n, last_n, location, Height)
        self.privileges = UserPrivileges()


class UserPrivileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(
            f"These are your privileges of Admin:\n{', '.join(self.privileges)}")


my_admin = Admin('Anh Quan', 'Thai', 'Sydney, Australia', 176)
my_admin.privileges.show_privileges()
'''
# 9-9
'''

from random import choice
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descrip_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model.upper()}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} Km on it")

    def update_odo(self, Kilom):
        if Kilom >= self.odometer_reading:
            self.odometer_reading = Kilom
        else:
            print("Nuh Uh")

    def incre_odo(self, Incre_km):
        self.odometer_reading += Incre_km

# child class


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} Km on full charge")

    def upgrade_batt(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"Battery upgraded to {self.battery_size}")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_porsch = ElectricCar("Porsche", 'Taycan', '2025')
my_porsch.battery.describe_battery()
my_porsch.battery.get_range()
my_porsch.battery.upgrade_batt()
my_porsch.battery.get_range()
'''

# IMPORTING CLASSES
'''
project/
│── car.py      class Car   
│── battery.py  class Battery:
│── electric_car.py from car import Car as C
                    from battery import Battery as B
'''

# Import MULTIPLE classes
'''
project/
│── car.py      class Car, class Battery:
│── electric_car.py from car import Car, Battery
'''

# IMPORT ENTIRE MODULE
'''
import file_name / import car
'''

# IMPORT ALL CLASSES FROM A MODULE
'''
form file_name import *
'''


# THE PYTHON STANDARD LIBRARY
'''
from random import randint
randint(1,6)
'''
'''
players = ['Charles Leclerc', 'Max Verstappen', 'Sonny Hayes', 'Jonny Pearces']
first_up = choice(players)
first_up
'''
