#!/opt/conda/bin/python
import sys

datoteka_in = sys.argv[1]

vsota = 0
stevilo = 0
for vrstica in open(datoteka_in):
    vsota = vsota + float(vrstica)
    stevilo = stevilo + 1
   
if stevilo > 0:
    print(vsota/stevilo)
    