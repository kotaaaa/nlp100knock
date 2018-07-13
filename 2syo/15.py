'''自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示するプログラム'''

import sys

args = sys.argv

print(args)
NUM = args[1]
print('第１引数：' + NUM)
f = open('input/hightemp.txt', 'r')
lines = f.readlines()
f.close()

all_line = []
f = open('hightemp_end_'+str(NUM)+'.txt','w')

print(int(NUM))
select_lines = []
for i in range(int(NUM)):
    index=i*-1
    index= index-1
    select_lines.append(lines[index])

for line in select_lines:
    all_line.append(line)
    f.write(line)
f.close()
