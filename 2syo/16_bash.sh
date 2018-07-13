#!/bin/sh

#途中です．エラーが出るかも．

# Nを入力
echo -n "N--> "
read n

# 行数算出　wcは行数とファイル名を出力するのでcutで行数のみ切り出し
# count=`wc --line input/hightemp.txt | cut --fields=1 --delimiter=" "`

# count=`wc -l input/hightemp.txt | cut -f 1 -d " "`
count=`wc -l input/hightemp.txt | cut -f 1 -d " "`
# 1分割当たりの行数算出　余りがある場合は行数を+1
echo $n
echo $count
unit=`expr $count / $n`
remainder=`expr $count % $n`
if [ $remainder -gt 0 ]; then
    unit=`expr $unit + 1`
fi
#
# # 分割
# split --lines=$unit --numeric-suffixes=1 --additional-suffix=.txt input/hightemp.txt child_test_
#
# # 検証
# for i in `seq 1 $n`
# do
#     fname=`printf child_%02d.txt $i`
#     fname_test=`printf child_test_%02d.txt $i`
#     diff --report-identical-files $fname $fname_test
# done
