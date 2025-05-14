#!/opt/conda/bin/python
cn = 0
s = 0
with open('teze.txt') as f:
    for line in f:
        print(line.strip())
        s += int(line.strip())
        cn += 1
print("sum:", s)
print("n:", cn)
print("average:", s/cn)