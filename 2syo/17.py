'''indexが入ってしまうので少し意図とずれますが，とりあえず先に進みます'''
import pandas as pd

# f = open('hightemp.txt', 'r')
# lines = f.readlines()
# f.close()

# hightemp = pd.read_table('input/hightemp.txt')
# print(hightemp)
cols = ['prefecture','city','degree','date']

hightemp = pd.read_table('input/hightemp.txt', header=None)
hightemp.columns = cols

# print(hightemp)

for col in cols:
    print(hightemp[col].value_counts())
    # print(type(hightemp[col].value_counts()))
    exit()
