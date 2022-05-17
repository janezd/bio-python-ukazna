#!/srv/conda/envs/notebook/bin/python
import sys

def prestej(s):
    frek = {}
    for c in s:
        frek[c] = frek.get(c, 0) + 1
    return frek

fin_name = sys.argv[1]
print(prestej(open(fin_name).read()))
