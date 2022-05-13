import json
import os

os.chdir("/Users/v/Documents/rosalind")
rna_prot = json.load(open("rna_prot.json"))

prot = 'MA'
combinations = list(rna_prot.values()).count('Stop')

for i in prot:
    keysList = [key for (key, value) in rna_prot.items() if value == i]
    combinations *= len(keysList)
