import pandas as pd

f = open('input/hightemp.txt', 'r')
lines = f.readlines()
f.close()
all_line = []
f = open('hightemp_out.txt','w')
for line in lines:
    New_line = line.replace('\t', ' ')
    # print(New_line)
    all_line.append(New_line)
    f.write(New_line)
# print(all_line)
f.close()
