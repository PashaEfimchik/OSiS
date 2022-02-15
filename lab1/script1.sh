#!/usr/bin/bash
file_count=0
subdirectories=-1
if [ -n "$1" ] 
then 
PATH="$1"
else 
PATH="/home/pavel/Документы/bsuir/OSiS/lab1/"
fi
for f in $(/bin/find $PATH -type f); do file_count=$[$file_count+1]; done
for d in $(/bin/find $PATH -type d); do subdirectories=$(($subdirectories+1)); done
/bin/find $PATH -type d > lab1.txt
/bin/find $PATH -type f >> lab1.txt
echo "Number of files:" $file_count >> lab1.txt
echo "Number of subdirectories:" $subdirectories >> lab1.txt
