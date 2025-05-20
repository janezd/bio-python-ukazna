#!/bin/bash
for filename in teze*.txt; do
    echo "--------------------------------"
    echo "Processing file: ${filename}"
    cat ${filename} | ./average2.py
done