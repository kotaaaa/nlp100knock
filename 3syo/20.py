import json

f = open('jawiki-country.json')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ
print('aaa')
for line in lines:
    data_json = json.loads(line)
    # print(data_json)
    # exit()
    if data_json['title'] == 'イギリス':
        print(data_json['text'])
        break

    # print(len(line))
    # print(type(line))
#
# exit()
# coding: utf-8
# import gzip
# import json
# fname = 'jawiki-country.json'
#
# with gzip.open(fname, 'rt') as data_file:
#     for line in data_file:
#         data_json = json.loads(line)
#         if data_json['title'] == 'イギリス':
#             print(data_json['text'])
#             break
