import json
import os

os.chdir("/Users/v/Documents/rosalind")
AS_mass = json.load(open("AS_mass.json"))

prot = 'SKADYEK'

mass = float()

for i in prot:
    mass += AS_mass[i]
