#!/bin/bash

for fn in datoteke/teze*.txt; do
    python average.py $fn
done