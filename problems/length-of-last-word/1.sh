#!/bin/bash

FILES="./in/*"
for f in $FILES
do
  #echo "Processing $f file..."

  out=$(eval "echo $f | grep -Eo [0-9]+")

  eval "python solution.py <$f | diff  -c out/output$out.txt -  "
done 

