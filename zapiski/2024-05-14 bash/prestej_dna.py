#!/opt/conda/bin/python
# prestej pojavitve a, t, c in g v dani datoteki
import sys

def prestej(zap):
    frek = {}
    for crka in zap:
        frek[crka] = frek.get(crka, 0) + 1
    return frek

dana_datoteka = sys.argv[1]
dano_zaporedje = open(dana_datoteka).read().strip()
print(prestej(dano_zaporedje))
