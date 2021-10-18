#!/bin/bash

command="ls";
eval "$command";
FILES="./in/*"
for f in $FILES
do
  #echo "Processing $f file..."
  # take action on each file. $f store current file name
  out=$(eval "echo $f | grep -Eo [0-9]+")

  eval "python3 solution.py <$f | diff  -c out/output$out.txt -  "
done 

