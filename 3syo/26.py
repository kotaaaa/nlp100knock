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


# def remove_markup(target):
#     '''マークアップの除去
#     強調マークアップを除去する
#
#     引数：
#     target -- 対象の文字列
#     戻り値：
#     マークアップを除去した文字列
#     '''
#
#     # 除去対象の正規表現のコンパイル
#     pattern = re.compile(r'''
#         \'{2,5} # 2〜5個の'
#         ''', re.MULTILINE + re.VERBOSE)
#
#     # 空文字に置換
#     return pattern.sub('', target)

def remove_markup(target):
    '''マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    '''

    # 除去対象の正規表現のコンパイル
    pattern = re.compile(r'''
        (\'{2,5})   # 2〜5個の'（マークアップの開始）
        (.*?)       # 任意の1文字以上（対象の文字列）
        (\1)        # 1番目のキャプチャと同じ（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)

    # 中身（2番目のキャプチャ内容）だけに置換
    return pattern.sub(r'\2', target)

# 基礎情報テンプレートの抽出条件のコンパイル
pattern = re.compile(r'''
    ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
    (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
    ^\}\}$      # '}}'の行
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# 基礎情報テンプレートの抽出
contents = pattern.findall(extract_UK())

# 抽出結果からのフィールド名と値の抽出条件コンパイル
pattern = re.compile(r'''
    ^\|         # '|'で始まる行
    (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
    \s*         # 空白文字0文字以上
    =
    \s*         # 空白文字0文字以上
    (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
    (?:         # キャプチャ対象外のグループ開始
        (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
    )           # グループ終了
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# フィールド名と値の抽出
fields = pattern.findall(contents[0])

# 辞書にセット
result = {}
keys_test = []      # 確認用の出現順フィールド名リスト
for field in fields:
    result[field[0]] = remove_markup(field[1])
    keys_test.append(field[0])

# 確認のため表示（確認しやすいようにkeys_testを使ってフィールド名の出現順にソート）
for item in sorted(result.items(),
        key=lambda field: keys_test.index(field[0])):
    print(item)
