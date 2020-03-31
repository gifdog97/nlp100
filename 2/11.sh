#!/bin/sh

TXTDIR=txtdata

FILENAME=hightemp.txt

# thinking_face
echo sed
sed s/"`printf '\t'`"/" "/g $TXTDIR/$FILENAME
echo

echo tr
tr '\t' ' ' < $TXTDIR/$FILENAME
echo

echo expand
expand -t 1 $TXTDIR/$FILENAME
echo
