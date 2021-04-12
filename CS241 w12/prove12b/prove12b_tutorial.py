import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place

'''This line isn't necessary, but it makes it so the later commands (e.g., read_csv)
are in a consistent place (You will obviously need to change this to the correct location on _your_ computer.)
If you have put the data files and your Python script in the same folder, you don't need this line.'''
# os.chdir("/Users/sburton/cs241/nbaData/")

'''
>>> import os
>>> os.getcwd()
'/home/user'
>>> os.chdir("/tmp/")
>>> os.getcwd()
'/tmp'
'''

# Load in the data
# The players data (basketball_players.csv) has the season stats
print('READING FILE')
players = pd.read_csv("basketball_players.csv")

print(players)

print()
print(players.columns)
print()

print('GETTING VALUES')
min = players["rebounds"].min()
max = players["rebounds"].max()
mean = players["rebounds"].mean()
median = players["rebounds"].median()

print("Rebounds per season: Min:{}, Max:{}, Mean:{:.2f}, Median:{}".format(min, max, mean, median))

'''
When working with existing columns, you can either use the dot notation "players.rebounds"
or the square bracket notation "players["rebounds"]". If you are creating a new column or
if your column name has a space in it, you must use the square bracket notation.
'''
print('--------------------------------------------------------')
print()

print('PRINTING TOP 10 VALUES FOR REBOUNDS')
data = players.sort_values("rebounds", ascending=False).head(10)
print(data)
print(data['rebounds'])
print('--------------------------------------------------------')
print()

print('GETTING A NEW SET FOR JUST SOME PLAYERS DATA')
print(players[['playerID', 'year', 'tmID', 'rebounds']].sort_values('rebounds', ascending=False).head(10))
print('--------------------------------------------------------')
print()

print('OPENING MASTER FILE DATA')
# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")
'''
players + master = nba
'''
print('--------------------------------------------------------')
print()

# We can do a left join to "merge" these two datasets together
print('MERGING PLAYERS AND MASTER DATA UNTO NBA')
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")
print(nba)
print(nba.columns)
print('--------------------------------------------------------')
print()

print(nba[['year', 'useFirst', 'lastName', 'tmID', 'rebounds']].sort_values('rebounds', ascending=False).head(10))
print('--------------------------------------------------------')
print()

nba['reboundsPerGame'] = nba['rebounds'] / nba['GP']
print(nba[['year', 'useFirst', 'lastName', 'rebounds', 'GP', 'reboundsPerGame']].sort_values('reboundsPerGame', ascending=False).head(10))
print('--------------------------------------------------------')
print()

# Let's just remove any rows with GP=0
nba = nba[nba.GP > 0]
nba['reboundsPerGame'] = nba['rebounds'] / nba['GP']
print('>>> Full data with rebounds')
print(nba)
print(nba[['year', 'useFirst', 'lastName', 'rebounds', 'GP', 'reboundsPerGame']].sort_values('reboundsPerGame', ascending=False).head(10))
print('--------------------------------------------------------')
print()


print('PLOTTING TIME!')
# PLOTTING
'''
nba.boxplot(column=["rebounds"])
'''
print('Plotting rebounds for full data')
print('>>> reboundsPerGame from nba')
sns.boxplot(data=nba.reboundsPerGame)
# Save the current plot to a file
plt.savefig("exportedImages/01_boxplot_reboundsPerGame.png")
print('Saving the boxplot as a png file')
# Show the current plot
plt.show()
# Adding more data
print('>>> adding more data to previous plot')
sns.boxplot(data=nba[['rebounds', 'oRebounds', 'dRebounds']])
plt.savefig("exportedImages/02_boxplot_reboundsPerGame_3boxplots.png")
plt.show()

# PLOTTING PARAMETERS
'''
Look in the internet for them.
'''
print('--------------------------------------------------------')
print()

# Get a subset of the data where the year is between 1980 and 1990
eighties = nba[(nba.year >= 1980) & (nba.year < 1990)]
print(eighties)
print('>>> plotting for 1980 decade')
sns.boxplot(eighties["reboundsPerGame"], orient="v")
plt.savefig("exportedImages/03_boxplot_reboundsPerGame_1980.png")
plt.show()
print('--------------------------------------------------------')
print()

grid = sns.FacetGrid(eighties, col="year")
grid.map(sns.boxplot, "reboundsPerGame", orient="v")
print('>>> plotting for each year of 1980 decade')
plt.savefig("exportedImages/04_boxplot_reboundsPerGame_1980_eachYear.png")
plt.show()
print('--------------------------------------------------------')
print()

nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").median()
print(nba_grouped_year)
print('--------------------------------------------------------')
print()

nba_grouped_year = nba_grouped_year.reset_index()
print(nba_grouped_year)
print('>>> linear regression plot for 1980 decade')
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame")
plt.savefig("exportedImages/05_linearRegression_reboundsPerGame_with0values.png")
plt.show()
print('--------------------------------------------------------')
print()

nba_grouped_year = nba_grouped_year[nba_grouped_year["reboundsPerGame"] > 0]
print('>>> linear regression plot without 0 values')
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame").set_title("Median rebounds per Year")
plt.savefig("exportedImages/06_linearRegression_reboundsPerGame_withOut0values.png")
plt.show()
print('--------------------------------------------------------')
print()

# group by max values
nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").max()
nba_grouped_year = nba_grouped_year.reset_index()
# Remove the zeros
nba_grouped_year = nba_grouped_year[nba_grouped_year["reboundsPerGame"] > 0]
print('>>> linear regression for top rebounders')
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame").set_title("Max rebounds per year")
plt.savefig("exportedImages/07_linearRegression_reboundsPerGame_forMaxRebounders.png")
plt.show()
print('--------------------------------------------------------')
print()

'''
nba_topRebounders_perYear
'''
# Get the top 10 rebounders per year
nba_topRebounders_perYear = nba[["reboundsPerGame", "year"]].groupby("year")["reboundsPerGame"].nlargest(10)

# Get the median of these 10
nba_topRebounders_median_perYear = nba_topRebounders_perYear.groupby("year").median()

# Put year back in as a column
nba_topRebounders_median_perYear = nba_topRebounders_median_perYear.reset_index()

# Again no zeros...
nba_topRebounders_median_perYear_noZeros = nba_topRebounders_median_perYear[nba_topRebounders_median_perYear["reboundsPerGame"] > 0]

# Now plot
print('>>> linear regression plot top 10 rebounder for 1980 decade, without 0 values')
sns.regplot(data=nba_topRebounders_median_perYear_noZeros, x="year", y="reboundsPerGame").set_title("Median of Top 10 Rebounders Each Year")
plt.savefig("exportedImages/08_linearRegression_reboundsPerGame_top10ReboundersMedian.png")
plt.show()
'''
This feels like a more accurate summary of the top rebounders each season,
 and it seems to help us answer our original question about rebounding trends.
  From this graphic we can show that the amount of rebounds per game among the
   top rebounders fluctuates a little, and peaked around 1970.
'''
print('--------------------------------------------------------')
print()

