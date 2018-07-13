# import pandas as pd
#
# f = open('hightemp.txt', 'r')
# lines = f.readlines()
# f.close()
# all_line = []
# f1 = open('col1.txt','w')
# f2 = open('col2.txt','w')
#
# for i, line in enumerate(lines):
#     if(i%2==0):
#         f1.write(line)
#     if(i%2==1):
#         f2.write(line)
#
# f1.close()
# f2.close()


import pandas as pd

hightemp = pd.read_table('input/hightemp.txt', header=None)
hightemp.columns = ['prefecture','city','degree','date']
# print(hightemp)
col1 = hightemp[['prefecture','degree']]
col2 = hightemp[['city','date']]
col1.to_csv('col1_retry.txt')
col2.to_csv('col2_retry.txt')
# print(hightemp[['prefecture','degree']])
