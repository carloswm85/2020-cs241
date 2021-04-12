

import pandas
import matplotlib.pyplot as plt

census_data = pandas.read_csv("census.csv",
                              header=None)

census_median = census_data[0].median()
print(census_median)

census_data.median().hist()
plt.show()
