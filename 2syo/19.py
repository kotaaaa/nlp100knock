import pandas as pd

cols = ['prefecture','city','degree','date']

hightemp = pd.read_table('input/hightemp.txt', header=None)
hightemp.columns = cols

# print(hightemp['prefecture'].value_counts())
hightemp_prefe = hightemp['prefecture'].value_counts()
# hightemp_prefe = hightemp_prefe.set_columns('prefecture')
print(hightemp_prefe)
print(hightemp_prefe.index)


hightemp = hightemp.sort_values(by='degree', ascending=False)
# print(hightemp)

# for col in cols:
#     print(hightemp[col].value_counts())
#     exit()
