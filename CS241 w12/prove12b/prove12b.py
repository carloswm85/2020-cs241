import pandas as pd
import seaborn as sns
import matplotlib as plt
import os

players = pd.read_csv('basketball_players.csv')
print(players)
print()
print(players.columns)
print()

print('>>> MEAN and MEDIAN POINTS FROM basketball_players.csv')
mean = players['points'].mean()
print(mean)
median = players['points'].median()
print(median)
print()

print('>>> MAX POINTS FROM basketball_players.csv')
max = players['points'].max()
print(max)
print()

print('>>> MIXING basketball_players.csv AND basketball_master.csv')
master = pd.read_csv('basketball_master.csv')
nba = pd.merge(players, master, how='left', left_on='playerID', right_on='bioID')
print(nba.columns)

print()
print('>>> Data player with max points')
index_max = nba.index[nba[nba['points'].max()]]
print(index_max)
# player_max = nba.loc[index_max, ['playerID', 'firstName', 'middleName', 'lastName', 'year', 'points']]
# print (data.loc[data[['rebounds']].idxmax(),["playerID", "year", "rebounds"]])
# print(player_max)
#
# print()
# print(nba[["year", "useFirst", "lastName", "tmID", "points"]].sort_values("points", ascending=False).head(5))

# print('>>> PLOTTING')
