for f in `awk {'print $1'} datoteke/qwerty-dna.txt`; do 
    grep "$f" datoteke/qwerty-dna.txt | awk {'print $2'} > $f.txt
done
