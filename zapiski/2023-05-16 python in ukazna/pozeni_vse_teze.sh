#!/bin/bash

set +e

for fn in datoteke/teze*txt; do
    echo -n $fn " "
    ./average.py $fn
done

