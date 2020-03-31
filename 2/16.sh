#!/bin/sh

TXTDIR=txtdata

FILENAME=hightemp.txt

OUTPUT_PY=split
OUTPUT_UNIX=split_unix

read N

lines=`cat $TXTDIR/$FILENAME | wc -l`
unit=$(($lines / $N))

if [ $(( $(($unit * $N)) != $lines )) ]; then
    unit=$(($unit + 1))
fi

# unix では d オプションを使えない
split -a 1 -l $unit $TXTDIR/$FILENAME $TXTDIR/$OUTPUT

last_suffix=$(printf "%b\n" $(printf "%s%x" "\\x" $((96+$N))))

# ブレース展開
# eval を使うと変数を使える
for alph in `eval echo {a..$last_suffix}`
do
    diff -s $TXTDIR/$OUTPUT_PY\_$alph $TXTDIR/$OUTPUT_UNIX\_$alph
done
    
