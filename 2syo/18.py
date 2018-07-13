import pandas as pd

cols = ['prefecture','city','degree','date']

hightemp = pd.read_table('input/hightemp.txt', header=None)
hightemp.columns = cols

hightemp = hightemp.sort_values(by='degree', ascending=False)
print(hightemp)

# for col in cols:
#     print(hightemp[col].value_counts())
#     exit()
