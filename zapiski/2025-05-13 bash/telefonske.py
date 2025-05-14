#!/opt/conda/bin/python
import sys
input_file = sys.stdin

data = {}

for line in input_file:
    name, number = line.split()

    if name in data:
        # key already in, just add to the list
        data[name].append(number)
    else:
        data[name] = [number]

print(data)