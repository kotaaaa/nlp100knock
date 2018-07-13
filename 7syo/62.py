# coding: utf-8
import re
import leveldb

fname_db = 'test_db'

# LevelDBオープン
db = leveldb.LevelDB(fname_db)

# valueが'Japan'のものを列挙
clue = 'Japan'.encode()
result = [value[0].decode() for value in db.RangeIter() if value[1] == clue]

pattern = re.compile(r'EX') # 0で始まり4で終わる最短の文字列
for i in result:
    matchObj = pattern.match(i)
    if matchObj:
        # print(matchObj)  # '01234'
        print(i)
# 件数表示
print('{}件'.format(len(result)))
