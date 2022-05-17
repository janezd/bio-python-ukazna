#!/bin/bash
for f in datoteke/qwerty-dna.txt; do
    echo "Procesiram $f"
    ./prestej_dna.py $f
done