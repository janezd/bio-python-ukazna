#!/srv/conda/envs/notebook/bin/python

import sys
fin = sys.stdin

sum = 0
cn = 0
for line in fin:
    sum += float(line)
    cn += 1

if cn > 0:
    print(sum/cn)
