import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place
# Load in the data
# The players data (basketball_players.csv) has the season stats
players = pd.read_csv("basketball_players.csv")
mean = players["points"].mean()
median = players["points"].median()
print("Points per season: Mean:{:.2f}, Median:{}".format(mean, median))
print("")

#print(players[["playerID", "year", "tmID", "points"]].sort_values("points", ascending=False).head(10))
master = pd.read_csv("basketball_master.csv")
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

print(nba[["year", "useFirst", "lastName", "tmID", "points"]].sort_values("points", ascending=False).head(10))
sns.boxplot(data=nba[["points", "assists", "rebounds"]])
plt.show()
nba_grouped_year = nba[["points", "year"]].groupby("year").median()
nba_grouped_year = nba_grouped_year.reset_index()
sns.regplot(data=nba_grouped_year, x="year", y="points")
plt.show()