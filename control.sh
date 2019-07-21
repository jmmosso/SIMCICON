#!/bin/sh
#find . -type f -name  | while read file;

while sleep 3
do
clear
echo "#######################################################"
echo "Salidas:"
#for f in `find . -name "ent*" -o -name "sal*" | sort`
for f in `find . -name sal* | sort`
do
  # output filename
  a=$(echo $f)
  # this prints the contents of the file to STD OUT
  b=$(cat $f)
  echo $a = $b
done

echo "#######################################################"
echo "Entradas:"
#for f in `find . -name "ent*" -o -name "sal*" | sort`
for f in `find . -name ent* | sort`
do
  # output filename
  a=$(echo $f)
  # this prints the contents of the file to STD OUT
  b=$(cat $f)
  echo $a = $b
done

done
