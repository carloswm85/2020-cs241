import pandas
import matplotlib.pyplot as plt
from datetime import datetime

data = pandas.read_csv('weather_year.csv')

'''
CONTENT:
    (A) Getting Started
    (B) Fun with Columns
    (C) Bulk Operations with apply()
    (D) Handing Missing Values
    (E) Accessing Individual Rows
    (F) Filtering
    (G) Grouping
    (H) Creating New Columns
    (I) Plotting
    (J) Getting Data Out
    (K) Miscellanea
'''

print('(A) GETTING STARTED')
print(data)
print()

print('>>> Length:')
print(len(data))
print()

print('>>> Column names:')
print(data.columns)
print()

print('>>> Accessing values on first column: Method 1')
print(data['EDT'])
print()

print('>>> Accessing values by passing a list of strings:')
print(data[['EDT', 'Mean TemperatureF']])
print()

print('>>> Accessing values on first column: Method 2')
print(data.EDT)
print()

print('PANDAS FUNCTIONS')
print('>>> Returns the first 5 items in a column')
print(data.EDT.head())
print()

print('>>> Returns the last 5 items in a column')
print(data.EDT.tail())
print()

print('>>> Returns the first n items in a column')
print(data.EDT.head(10))
print()

print('>>> Using dictionary syntax')
print(data['Mean TemperatureF'].head())
print()

print('(B) FUN WITH COLUMNS')
print(">>> Changing column's names")
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]
print(data)
print()

print('>>> First 5 values for mean_temp')
print(data.mean_temp.head())
print()

print('>>> Get standard deviation')
print(data.mean_temp.std())
print()

print('>>> Plot as an histogram and display it')
data.mean_temp.hist()
# plt.show()
print()

print('>>> std for the entire DataFrame')
print(data.std())
print()

print('(C) BULK OPERATIONS WITH apply()')
print('>>> Display first 5 dates')
print(data.date.head())
print()

print('>>> Displays the very first value for dates')
first_date = data.date.values[0]
print(first_date)
print()

print('>>> Format the original date into Python datetime format')
datetime.strptime(first_date, '%Y-%m-%d')
print(datetime.strptime(first_date, '%Y-%m-%d'))
print()

print('>>> Now do the same to the entire DataFrame')
print(data.date)
print('Now change it!')
data.date = data.date.apply(lambda d: datetime.strptime(d, '%Y-%m-%d'))
print(data.date)
print()

print('>>> Change the index from 0 to n, to the newly made dates')
data.index = data.date
print(data)
print()

print('>>> Find the information to a given row')
print('NOTE: loc[] replaces ix[] property')
print(data.loc[datetime(2012, 8, 19)])
print()

print('>>> Delete or drop a column')
data = data.drop('date', axis=1)
print(data)
print()

print('(D) HANDING MISSING VALUES')
print('>>> Tell what values are null: True or False')
empty = data.apply(lambda col: pandas.isnull(col))
print(empty)
print()

print('>>> Display first "empty" 10 in events column')
print(empty.events.head(10))
print()

print('>>> Display first 10 events from the DataFrame')
print(data.events.head(10))
print()

print('>>> Delete ALL rows with NaN values on the "events" column')
print(data.dropna(subset=['events']))
print()

print('>>> Fills the NaN values in the "events" column with empty strings')
data.events = data.events.fillna('')
print(data.events.head(10))
print()

print('(E) ACCESSING INDIVIDUAL ROWS')
print('>>> Grab a given row')
print(data.iloc[0, :])
print()

print('>>> Using the index value')
print(data.loc[datetime(2013, 1, 1)])
print()

print('>>> Getting information with a loop')
num_rain = 0
for idx, row in data.iterrows():
    # iterrows() returns 2 values
    # it returns the index and the entire row
    if "Rain" in row["events"]:
        num_rain += 1
print("Days with rain: {0}".format(num_rain))
print()

print('(F) FILTERING')
print('>>> Selecting rows of interest, using dictionary syntax')
print('>>> max_temp <= 32')
freezing_days = data[data.max_temp <= 32]
print(freezing_days)
print()

print('>>> More filtering')
print('>>> min_temp >= 20')
freezing_days = freezing_days[freezing_days.min_temp >= 20]
print(freezing_days)
print()

print('>>> Both condition can be applied simultaneously')
print('>>> max_temp <= 32 & min_temp >= 20')
freezing_days = data[(data.max_temp <= 32) & (data.min_temp >= 20)]
print(freezing_days)
print()

print('>>> What type of object we are really getting')
print(type(data.max_temp <= 32))
print()

print('>>> What is inside the filter')
print('Our filter is nothing more than a Series with a boolean value for every item in the index.')
print(data.max_temp <= 32)
print()

print('>>> This should be a series, but it is not... THIS is NOT working')
temp_max = data.max_temp <= 32
print(data[temp_max])
print()

print('>>> Another filter')
temp_min = data.min_temp >= 20
print(temp_min)
print()

print('>>> Using &')
temp_min = data.min_temp >= 20
temp_max = data.max_temp <= 32
print(temp_min & temp_max)
print()

print('>>> Using |')
temp_min = data.min_temp >= 20
temp_max = data.max_temp <= 32
print(temp_min | temp_max)
print()

print('>>> The any() function returns True if any value in the Series is True')
temp_both = temp_min & temp_max
print(temp_both.any())
print()

print('>>> Using apply on filtering "Rain"')
print(data[data.events.apply(lambda e: "Rain" in e)])
print()


print('(G) GROUPING')
print('>>> Groups by value on the designated column')
print('>>>'
      'cover: int'
      'cover_data: pandas.core.frame.DataFrame'
      'cover_temps: dict')
print(data)
cover_temps = {}
for cover, cover_data in data.groupby("cloud_cover"):
    '''When you iterate through the result of groupby(),
    you will get a tuple. The first item is the column value,
    and the second item is a filtered DataFrame
    (where the column equals the first tuple value).'''
    cover_temps[cover] = cover_data.mean_temp.mean()  # The mean mean temp!
print(cover_temps)
print()

print('>>> Grouping by more than one column')
print('>>>'
      'cover: numpy.int64'
      'events: srt'
      'group_data: pandas.core.frame.DataFrame')
print(data.columns)
for (cover, events), group_data in data.groupby(["cloud_cover", "events"]):
    print ("Cover: {0}, Events: {1}, Count: {2}".format(cover, events, len(group_data)))
print()

print('(H) CREATING NEW COLUMNS')
print('>>> Discover the different kinds of values')
print(data.events.unique())
print()

print('>>> Creating new columns for any given values')
print(data)
print()
for event_kind in ["Rain", "Thunderstorm", "Fog", "Snow"]:
    col_name = event_kind.lower()  # Turn "Rain" into "rain", etc.
    data[col_name] = data.events.apply(lambda e: event_kind in e)
print(data)
print('> 4 more columns have been created')
print()
print('> All columns names are: ')
print(data.columns)
print()
print('> New column, accessible with dot syntax')
print(data.rain)
print()

print('>>> How many days had rain')
print(data.rain.sum())
print()

print('>>> How many days had rain and snow')
print(data[data.rain & data.snow])

print('(I) PLOTTING')
print('>>> Line plot')
print(type(data.max_temp.plot()))
'''The plot() function returns a matplotlib AxesSubPlot object.
You can pass this object into subsequent calls to plot() in order to compose plots.'''
plt.show()
'''That one line of code did a lot for us.
First, it created a nice looking line plot using the maximum temperature column from our DataFrame.
Second, because we used datetime objects in our index, pandas labeled the x-axis appropriately.'''
print()

print('>>> Line plotting last 5 values')
print(data.max_temp.tail().plot())
plt.show()
print()

print('>>> Bar plot')
print(data.max_temp.tail().plot(kind='bar', rot=10))
plt.show()
print()

print('>>> Customizing parameters')
ax = data.max_temp.plot(title="Min and Max Temperatures")
data.min_temp.plot(style="red", ax=ax)
ax.set_ylabel("Temperature (F)")
plt.show()
print()

print('(J) GETTING DATA OUT')
print('>>> Saving data into csv file')
data.to_csv("weather-mod.csv")
print()

print('>>> Make it tab separated instead')
data.to_csv("weather-mod.tsv", sep="\t")
print()

print('(K) MISCELLANEA')
print('>>> Modify the original "row" and not just a copy of it')
'''
    idx: pandas._libs.tslibs.timestamps.Timestamp
    row: pandas.core.series.Series
'''
for idx, row in data.iterrows():
    data.loc[idx, "max_temp"] = 0
print(any(data.max_temp != 0))  # Any rows with max_temp not equal to zero?
print()

print('>>> Using apply() to go over COLUMNS')
print(data.apply(lambda c: c.name))
print()

print('>>> Using apply() to go over ROWS')
print(data.apply(lambda r: r["max_pressure"] - r["min_pressure"], axis=1))
print()

print('>>> Dropping a row')
print(data)
# data.drop([])
print(data)