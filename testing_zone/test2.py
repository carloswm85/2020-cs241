from pandas.io import sql
import sqlite3

conn = sqlite3.connect('/myDataSource')
query = "SELECT * FROM towed WHERE make = 'FORD';"

results = sql.read_sql(query, con=conn)
results.head()



