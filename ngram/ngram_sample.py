import re

sentense = "I am an NLPer"

def ngram(sentense, scale, type):
    # 関数の第三引数typeがwordの場合
    if type == 'word':

        # 変数を用意
        str = ''
        wordlist = []

        # 文章からピリオドを除外して空白で分割
        splited = re.split('\s', sentense.replace('.', ''))

        # もし第二引数の値が文章内の単語数より少なければエラーを出す
        if scale > len(splited):
            print("ERROR: The argument, scale must be lawer than the actual number of the words in the argument, sentense.")
        else:
            for i in range (0, len(splited)-(scale-1)):
                for ii in range (0, scale):
                    if ii == 0:
                        str += splited[ii+i]
                    else:
                        str += ' ' + splited[ii+i]
                wordlist.insert(i, str)
                # strを初期化
                str = ''

            return wordlist

    # 関数の第三引数typeがcharの場合
    elif type == 'char':
        charlist = []
        # 文字nグラムを作成
        trimed = (sentense.replace(' ', '')).replace('.', '')

        if scale > len(trimed):
            print("ERROR: The argument, scale must be lawer than the actual number of the characters in the argument, sentense.")
        else:
            for iii in range (0, len(trimed)-(scale-1)):
                charlist.insert(iii, trimed[iii:iii+scale])

            return charlist

    # 関数の第三引数typeがword/charでない場合エラーを出す
    else:
        print("ERROR: The 3rd argument, type must be char or word.")

data1 = ngram(sentense, 2, "word")
data2 = ngram(sentense, 2, "char")
