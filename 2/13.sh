#!/bin/sh

TXTDIR=txtdata

COL1_FN=col1.txt
COL2_FN=col2.txt

MERGE_FN=merge.txt
MERGE_UNIX_FN=merge_unix.txt

paste $TXTDIR/$COL1_FN $TXTDIR/$COL2_FN > $TXTDIR/$MERGE_UNIX_FN

diff -s $TXTDIR/$MERGE_FN $TXTDIR/$MERGE_UNIX_FN
