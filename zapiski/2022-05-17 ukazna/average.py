#!/srv/conda/envs/notebook/bin/python

import sys
fin_name = sys.argv[1]

sum = 0
cn = 0
for line in open(fin_name):
    sum += float(line)
    cn += 1

if cn > 0:
    print(sum/cn)