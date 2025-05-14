#!/bin/bash
declare -i sum
declare -i cn

sum=0
while read line; do
    sum=$sum+$line
    echo $line
    cn=$cn+1
done < teze.txt

echo "sum: $sum"
echo "n:" $cn
echo "average:" $[ $sum/$cn ]

