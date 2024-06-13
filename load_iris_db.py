import sqlite3
import pandas as pd

# Code to load 

con = sqlite3.connect('./database.sqlite')
cur = con.cursor()
df = pd.read_csv('./Iris.csv')
df.to_sql('Iris', con, if_exists='append', index=False)
con.commit()