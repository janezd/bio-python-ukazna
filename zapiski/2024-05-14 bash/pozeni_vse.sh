for f in datoteke/qwerty-dna/*.txt; do
    echo $f
    ./prestej_dna.py $f
done