#!/opt/conda/bin/python
import sys

fin = sys.stdin

cn = 0
s = 0
for line in fin:
    v = line.strip()
    print(v)
    s += int(v)
    cn += 1
print("sum:", s)
print("n:", cn)
print("average:", s/cn)
