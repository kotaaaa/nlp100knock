# coding: utf-8
import math

fname = 'input/hightemp.txt'
n = int(input('N--> '))

print(n)
with open(fname) as data_file:
    lines = data_file.readlines()

count = len(lines)
print(count)
unit = math.ceil(count / n)  # 1ファイル当たりの行数

for i, offset in enumerate(range(0, count, unit), 1):
    with open('output/child_{:02d}.txt'.format(i), mode='w') as out_file:
        for line in lines[offset:offset + unit]:
            # print(offset)
            # print(line)
            out_file.write(line)


'''このソースの元のページ(参考にさせて頂いたサイト)(参考になりました．ありがとうございます．)
https://qiita.com/segavvy/items/993ea169a1111c6f6f69
'''
