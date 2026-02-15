# THIS CHAP, DOWNLOAD DATA SETS ONLINE SOURCES AND CREATE WORKING VISUALIZATIONS OF THAT DATA
# To find patterns and connections

# We'll access and visualize data stored in CSV and JSON


# THE CSV FILE FORMAT
# for eg a chunk of weather data in CSV format
'''
"USW00025333","SITKA AIRPORT, AK US","2018-01-01","0.45",,"48","38"
'''

# Parsing the CSV file headers
import csv
from datetime import datetime
import matplotlib.pyplot as plt


'''
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

# Printing the Headers and Their positions
   
    for index, column_header in enumerate(header_row):
        print(index, column_header)
   
# Extracting and Reading Data
# get high temps from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# plot the high temps
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# format plot
plt.title("Daily high temp, July 2018", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperture (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''

# The datetime Module
# from datetime import datetime
'''
first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)
'''

# Plotting dates
'''
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    # Get date and htemp from the file
    dates, highs, lows = [], [], []
    for row in reader:
        curr_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(curr_date)
        highs.append(high)
        lows.append(low)

# plot high temp
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Shading region. Alpha = transparent intensity
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='Blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='Blue', alpha=0.1)

# format plot
ax.set_title("Daily high tempertures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperture (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''

# Error checking
'''
filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get date and htemp from the file
    dates, highs, lows = [], [], []
    for row in reader:
        curr_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Sorry, missing data for {curr_date}')
        else:
            dates.append(curr_date)
            highs.append(high)
            lows.append(low)

# plot high temp
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Shading region. Alpha = transparent intensity
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='Blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='Blue', alpha=0.1)

# format plot
# x.set_title(
#    "Daily high and low tempertures - 2018\nDeath Valley, CA", fontsize=20)
plt.title("Daily high and low tempertures - 2018\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperture (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''

# 16-1:
# here i got an error about misplacing int instead of a float, because precipitation is a float and i haven't even take a look the data so first i gotta take a look first

'''
fn = 'data/sitka_weather_2018_simple.csv'
with open(fn) as f:
    reader = csv.reader(f)
    header_row = next(reader)
#    for index, column_header in enumerate(header_row):
#       print(index, column_header)

    dates, precip = [], []

    for row in reader:
        #        print(row)
        #        break       use this to take a look of the data

        curr_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcp = float(row[3])
        except ValueError:
            print(f"There's no data for {curr_date}")
        else:
            dates.append(curr_date)
            precip.append(prcp)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, precip, c="red")
plt.title("Daily precipitation - 2018", fontsize=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Precipitation', fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)

plt.show()
'''


# 16-2
'''
fsitka = 'data/sitka_weather_2018_simple.csv'
fdeath = 'data/death_valley_2018_simple.csv'

with open(fsitka) as f1:
    reader1 = csv.reader(f1)
    head_row1 = next(reader1)

    dates1, highs1, lows1 = [], [], []
    for row in reader1:
        curr_date1 = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high1 = int(row[5])
            low1 = int(row[6])
        except ValueError:
            print(f"Data unavailable for {curr_date1}")
        else:
            dates1.append(curr_date1)
            highs1.append(high1)
            lows1.append(low1)


with open(fdeath) as f2:
    reader2 = csv.reader(f2)
    head_row2 = next(reader2)

    dates2, highs2, lows2 = [], [], []
    for row in reader2:

        curr_date2 = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high2 = int(row[4])
            low2 = int(row[5])
        except ValueError:
            print(f'Data unavailable for {curr_date2}')
        else:
            dates2.append(curr_date2)
            highs2.append(high2)
            lows2.append(low2)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates1, highs1, c='red')
ax.plot(dates1, lows1, c='Orange')
plt.fill_between(dates1, highs1, lows1, facecolor='Yellow', alpha=0.5)

ax.plot(dates2, highs2, c='Green')
ax.plot(dates2, lows2, c='Blue')
plt.fill_between(dates2, highs2, lows2, facecolor='Pink', alpha=0.5)

plt.title('Sitka vs Death valley temperture', fontsize=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Temperture (F)', fontsize=14)


plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
'''


#  16-3
'''
fn = ('data/San_Francisco_weather_data.csv')
with open(fn) as f:
    reader = csv.reader(f)
    header = next(reader)
    print (header)
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
            
        except ValueError:
            print(f'data unavailable for {date}')

        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
plt.style.use('seaborn-v0_8')
fig, ax= plt.subplots()

ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='Yellow', alpha = 1)

plt.title("San Francisco Temp", fontsize = 24)
plt.xlabel("Date", fontsize = 14)
plt.ylabel("Temperture (F)", fontsize = 14)

plt.tick_params(axis='both', which= 'major', labelsize=10)

plt.show()
'''


#16-4
'''
fn = ('data/San_Francisco_weather_data.csv')
with open(fn) as f:
    reader = csv.reader(f)
    header = next(reader)

    date_index = header.index('DATE')
    high_ind = header.index('TMAX')
    low_ind = header.index('TMIN')
    name_ind = header.index('NAME')
    
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_ind])
            low = int(row[low_ind])
            name = str(row[name_ind])
        except ValueError:
            print(f'data unavailable for {date}')

        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
plt.style.use('seaborn-v0_8')
fig, ax= plt.subplots()

ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='Yellow', alpha = 1)

plt.title(f"High & Low temperture - {name}", fontsize = 16)
plt.xlabel("Date", fontsize = 14)
plt.ylabel("Temperture (F)", fontsize = 14)

plt.tick_params(axis='both', which= 'major', labelsize=10)

plt.show()
'''



#Mapping Global Data Sets: JSON Format

#downloading earthquake data
#loading and displaying
'''
import json

#Explore the structure of the data
fn = 'data/eq_data_1_day_m1.json'
with open(fn) as f:
    all_eq_data = json.load(f) #Store converted data into python format, this case a giant dict
#Making a list of all eqs
all_eq_dicts = all_eq_data['features']

readable_file = 'data/readable_eq_data.json' 
with open(readable_file, 'w') as f:      
    json.dump(all_eq_data, f, indent=4)

#Extracting magnitude & location data
mags, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)

#Building a world map
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#map the eqs
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'marker':{
        'size': [5*mag for mag in mags] #customizing marker size for easier reading
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquake.html')
'''
#Import scattergeo chart type and the layout class, offline module to render the map = making a barcha

#A different way of specifying chart data

#data= [Scattergeo(lon=longs, lat=lats)]
#Equivilant to
'''
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
}]
'''

'''
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)

#Customizing marker color
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat':lats,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
    },
}]
my_lay = Layout(title= 'Global Earthquakes')

fig = {'data':data, 'layout': my_lay}
offline.plot(fig, filename='global_earthquake30ds.html')
'''

#Other colorscales
'''
from plotly import colors
for k in colors.PLOTLY_SCALES.keys():
    print(k)
'''


#Adding Hover Text
'''
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, longs, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
   # title = eq_dict['properties']['title']
    mags.append(mag)
    longs.append(long)
    lats.append(lat)
    #hover_texts.append(title)

#Customizing marker color
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat':lats,
    #'text': hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
    },
}]
my_lay = Layout(title= 'Global Earthquakes')

fig = {'data':data, 'layout': my_lay}
offline.plot(fig, filename='global_earthquake30ds.html')
'''


#16-6