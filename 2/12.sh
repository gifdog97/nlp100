#!/bin/sh

TXTDIR=txtdata

FILENAME=hightemp.txt
COL1_FN=col1.txt
COL2_FN=col2.txt

COL1_UNIX_FN=col1_unix.txt
COL2_UNIX_FN=col2_unix.txt

cut -f 1 $TXTDIR/$FILENAME > $TXTDIR/$COL1_UNIX_FN
cut -f 2 $TXTDIR/$FILENAME > $TXTDIR/$COL2_UNIX_FN

diff -s $TXTDIR/$COL1_FN $TXTDIR/$COL1_UNIX_FN
diff -s $TXTDIR/$COL2_FN $TXTDIR/$COL2_UNIX_FN
