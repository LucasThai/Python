from plotly.graph_objs import Scatter, Layout
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
from random import randint
from RandomWalk import RandomWalk
import matplotlib.pyplot as plt

# Plotting simple line graph
'''
# y-values, plt auto creates x-values [0, 1, 2, 3, 4] if there's none
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)  # thickness of the line

# set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()
'''


# Plotting and styling individual points with scatter()
'''
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# set chart title and label axes
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

ax.tick_params("both", which='major', labelsize=14)

plt.show()
'''

# Plotting a series of points with scatter()
'''
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and lable axes
ax.set_title("Square number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''


# Calculating data automatically
'''
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Set chart title and lable axes
ax.set_title("Square number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)
# ax.axis([0, 1100, 0, 1100000]) runs x axis from 0 to 1100 and y axis from 0 to 1100000

plt.show()
'''

# Defining custom colors
# ax.scatter(x_values, y_values, c='red', s = 10) or c=(0, 0.8, 0)

# Using a Colormap
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) looks like gradient


# Saving ur plots Auto
# replace plt.show() with plt.savefig("squares_plot.png", bbox_inches = 'tight')


# 15-1
'''
x_values = range(0, 5)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=100)

# Title
ax.set_title("Cubic numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubic values", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''
# AND
'''
x_values = range(0, 5000)
y_values = [x**3 for x in x_values]

# style
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# draw
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# label
ax.set_title("Cubic numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel('Cubic of values', fontsize=14)

# set tick
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''

# 15-2: Done


# RANDOM WALKS
# is a path has no clear direction but is determined by a series of random decisions

# Creating the RandomWalk() class
'''
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # plot the points in the walk.
    plt.style.use('classic')

    # altered the size to fill the screen
    fig, ax = plt.subplots(figsize=(15, 9))

    pointnumbers = range(rw.num_points)
    ax.scatter(rw.xvalues, rw.yvalues, c=pointnumbers,
               cmap=plt.cm.Blues, edgecolors='face', s=50)

    # ax.scatter(rw.xvalues, rw.yvalues, s=15)

    # plotting first and last points
    ax.scatter(0, 0, c='red', edgecolors='none', s=50)
    ax.scatter(rw.xvalues[-1], rw.yvalues[-1],
               c='green', edgecolors='none', s=50)

    # Cleaning up the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_runnin = input(Make another walk? \nY/N?").strip().lower()
    if keep_runnin == 'n':
        break
'''

# 15-3 &  15-4 & 15-5 -> Satisfied

'''
rw = RandomWalk()
rw.fill_walk()

# setting style of figure
plt.style.use("classic")
fig, ax = plt.subplots(figsize=(10, 5), dpi=192)

# main plot
point_numbers = range(rw.num_points)
# ax.scatter(rw.xvalues, rw.yvalues, c=point_numbers,
#           cmap=plt.cm.Blues, edgecolors='face', s=20)
ax.plot(rw.xvalues, rw.yvalues, linewidth=2, color='blue')

# since we need to iden first and last point
ax.scatter(0, 0, c='red', edgecolors='none', s=50)
ax.scatter(rw.xvalues[-1], rw.yvalues[-1],
           c='black', edgecolors='none', s=50)

# we do need the axes tho but let's just delete those
# ax.get_xaxis().set_visible(false)
# ax.get_yaxis().set_visible(false)

plt.show()
'''

# Rolling Dice with Plotly

'''
die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


print(frequencies)
'''

# Making a histogram
# from plotly.graph_objs import Bar, Layout
# from plotly import offline
'''
die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of results'}
my_layout = Layout(title='Result of rolling D6 100 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({"data": data, 'layout': my_layout}, filename='d6.html')
'''


# Rollin 2 dice

# create 2 dice
'''
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# controls spacing between tick marks on x-axis
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_lay = Layout(title='Results of rolling two D6 100 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_lay}, filename='d6.html')
'''

# Rolling dice of different sizes
'''
die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(100):
    result = die1.roll()+die2.roll()
    results.append(result)

frequencies = []
max_value = die1.num_sides + die2.num_sides
for value in range(2, max_value+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_value+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_lay = Layout(title='Results of rolling a D6 and a D10 100 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_lay}, filename='d6d10.html')
'''

# 15-6
'''
die1 = Die(8)
die2 = Die(8)

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_value = die1.num_sides + die2.num_sides
for value in range(2, max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

xvalues = (list(range(2, max_value+1)))
data = [Bar(x=xvalues, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_lay = Layout(title='Results of rolling two D8 1000 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_lay}, filename='d8x2.html')
'''

# 15-7
'''
d1 = Die()
d2 = Die()
d3 = Die()

results = []
for roll_num in range(1000):
    result = d1.roll()+d2.roll()+d3.roll()
    results.append(result)

frequencies = []
max_va = d1.num_sides + d2.num_sides + d3.num_sides
for value in range(3, max_va+1):
    frequency = results.count(value)
    frequencies.append(frequency)

xval = list(range(3, max_va+1))
data = [Bar(x=xval, y=frequencies,)]

x_ax_conf = {'title': 'Results', 'dtick': 1}
y_ax_conf = {'title': 'Frequencies of result'}
my_lay = Layout(title="Frequency of result of rolling 3 D6 at 1000 times",
                xaxis=x_ax_conf, yaxis=y_ax_conf)

offline.plot({'data': data, 'layout': my_lay}, filename='D6x3.html')
'''


# 15-8
'''
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# controls spacing between tick marks on x-axis
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_lay = Layout(title='Results of rolling two D6 100 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_lay}, filename='d6.html')
'''

# 15-9:
'''
die = Die()
results = [die.roll() for _ in range(100)]
for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of results'}
my_layout = Layout(title='Result of rolling D6 100 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({"data": data, 'layout': my_layout}, filename='d6.html')
'''

# 15-10
'''
die = Die()

results = [die.roll() for _ in range(1000)]
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

x_values = list(range(1, die.num_sides+1))
y_values = frequencies

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=100)
ax.plot(x_values, y_values, linewidth=2)

ax.set_title("Frequency of result of a D6 roll for 1000 times", fontsize=20)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of result", fontsize=14)

ax.tick_params(axis='x', which='major', labelsize=14)

plt.show()
'''

# And

'''
rw = RandomWalk()
rw.fill_walk()

x_val = rw.xvalues
y_val = rw.yvalues

data = [
    Scatter(
        x=x_val,
        y=y_val,
        mode="lines",
        line={"width": 2},
        name="Random Walk"
    )
]

layout = Layout(
    title="Random Walk",
    xaxis={"title": "Position X"},
    yaxis={"title": "Position Y"}
)

offline.plot(
    {"data": data, "layout": layout},
    filename="RandomWalk.html"
)
'''
