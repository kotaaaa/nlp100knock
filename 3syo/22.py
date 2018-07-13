# coding: utf-8
import json
import re

def extract_UK():
    '''イギリスに関する記事本文を取得
        戻り値：
        イギリスの記事本文'''
    f = open('jawiki-country.json')
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    # lines2: リスト。要素は1行の文字列データ
    for line in lines:
        data_json = json.loads(line)
        # print(data_json)
        # exit()
        if data_json['title'] == 'イギリス':
            # print(data_json['text'])
            return data_json['text']

    # print(len(line))
    raise ValueError('イギリスの記事が見つからない')
# 正規表現のコンパイル
pattern = re.compile(r'''
    ^       # 行頭
    .*      # 任意の文字0文字以上
    \[\[Category:
    (       # キャプチャ対象のグループ開始
    .*?     # 任意の文字0文字以上、非貪欲マッチ（貪欲にすると後半の'|'で始まる装飾を巻き込んでしまう）
    )       # グループ終了
    (?:     # キャプチャ対象外のグループ開始
    \|.*    # '|'に続く0文字以上
    )?      # グループ終了、0か1回の出現
    \]\]
    .*      # 任意の文字0文字以上
    $       # 行末
    ''', re.MULTILINE + re.VERBOSE)

# 抽出
result = pattern.findall(extract_UK())

# 結果表示
for line in result:
    print(line)
