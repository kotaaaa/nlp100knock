import pandas as pd

hightemp = pd.read_table('input/hightemp.txt', header=None)
hightemp.columns = ['prefecture','city','degree','date']
# print(hightemp)
print('hightempの要素数:',len(hightemp.index))
print('hightempの要素数:',len(hightemp.index))
