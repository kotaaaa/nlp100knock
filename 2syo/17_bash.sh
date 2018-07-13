#!/bin/sh

#途中です．エラーが出るかも．

# 先頭カラムを切り出し、ソート、重複除去
cut --fields=1 input/hightemp.txt | sort | uniq > result_test.txt

# Pythonのプログラムで実行、diffで比較するためにソート
python main.py | sort > result.txt

# 結果の確認
diff --report-identical-files result.txt result_test.txt
