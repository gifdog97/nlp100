#!/bin/sh

TXTDIR=txtdata

FILENAME=hightemp.txt

cut -f 1 $TXTDIR/$FILENAME | sort -u

