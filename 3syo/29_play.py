# coding: utf-8
import json
import re
import urllib.parse, urllib.request

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

def remove_markup(target):
    '''マークアップの除去
    MediaWikiマークアップを可能な限り除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    '''

    # 強調マークアップの除去
    pattern = re.compile(r'''
        (\'{2,5})   # 2〜5個の'（マークアップの開始）
        (.*?)       # 任意の1文字以上（対象の文字列）
        (\1)        # 1番目のキャプチャと同じ（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\2', target)

    # 内部リンク、ファイルの除去
    pattern = re.compile(r'''
        \[\[        # '[['（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上、非貪欲
            \|      # '|'
        )*?         # グループ終了、このグループが0以上出現、非貪欲
        ([^|]*?)    # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \]\]        # ']]'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)

    # Template:Langの除去        {{lang|言語タグ|文字列}}
    pattern = re.compile(r'''
        \{\{lang    # '{{lang'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上、非貪欲
            \|      # '|'
        )*?         # グループ終了、このグループが0以上出現、非貪欲
        ([^|]*?)    # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \}\}        # '}}'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)

    # 外部リンクの除去  [http://xxxx] 、[http://xxx xxx]
    pattern = re.compile(r'''
        \[http:\/\/ # '[http://'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^\s]*? # 空白以外の文字が0文字以上、非貪欲
            \s      # 空白
        )?          # グループ終了、このグループが0か1出現
        ([^]]*?)    # キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
        \]          # ']'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)

    # <br>、<ref>の除去
    pattern = re.compile(r'''
        <           # '<'（マークアップの開始）
        \/?         # '/'が0か1出現（終了タグの場合は/がある）
        [br|ref]    # 'br'か'ref'
        [^>]*?      # '>'以外が0文字以上、非貪欲
        >           # '>'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub('', target)

    return target


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
    # keys_test.append(field[0])

# 国旗画像の値を取得
fname_flag = result['国旗画像']
print(fname_flag)
print(urllib.parse.quote(fname_flag))
# exit()

# リクエスト生成
# url = 'https://www.mediawiki.org/w/api.php?' \
#     + 'action=query' \
#     + '&titles=File:' + urllib.parse.quote(fname_flag) \
#     + '&format=json' \
#     + '&prop=imageinfo' \
#     + '&iiprop=url'

url = 'http://ja.wikipedia.org/w/api.php?format=json&action=query&prop=info&titles=%E3%82%A8%E3%83%9E%E3%83%BB%E3%83%AF%E3%83%88%E3%82%BD%E3%83%B3'


# MediaWikiのサービスへリクエスト送信
request = urllib.request.Request(url,
    headers={'User-Agent': 'NLP100_Python(@kotaaa)'})
connection = urllib.request.urlopen(request)

print(connection)
print(connection.read().decode())
# # jsonとして受信
# connection = str(connection).replace("'", '"')#.replace('True', 'true').replace('False', 'false')
connection = str(connection).replace('"',"'")
data = json.loads(connection)
data = json.loads(connection.read().decode())
# data = json.loads(connection.read())
#
#
# # URL取り出し
# url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
# print(url)
