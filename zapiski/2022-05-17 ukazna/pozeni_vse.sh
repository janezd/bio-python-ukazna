#!/bin/bash

for fn in datoteke/teze*.txt; do
    python average.py $fn
    # ./average.py $fn
    # cat $f | ./average.py
done
