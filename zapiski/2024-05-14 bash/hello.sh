declare -i sum
declare -i cn

sum=0
while read line; do
    sum=$sum+$line
    echo $line
    cn=$cn+1
done < datoteke/teze.txt

echo "vsota: $sum"
echo "n:" $cn
echo "povprecje:" $[ $sum/$cn ]

