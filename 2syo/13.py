'''indexが入ってしまうので少し意図とずれますが，とりあえず先に進みます'''
import pandas as pd

# f = open('hightemp.txt', 'r')
lines = f.readlines()
f.close()
all_line = []
f1 = open('output/col1.txt','r')
lines = f1.readlines()
f1.close()

f2 = open('output/col2.txt','r')
lines = f2.readlines()
f2.close()


for i, line in enumerate(lines):
    if(i%2==0):
        f1.write(line)
    if(i%2==1):
        f2.write(line)

f1.close()
f2.close()
