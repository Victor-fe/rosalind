import pandas as pd

dna = 'TCAATGCATGCGGGTCTATATGCAT'
dna = list(dna)
complement = list(dna)

complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

for i in range(0, len(complement)):
    if complement[i] == 'A':
        complement[i] = complements['A']
    elif complement[i] == 'C':
        complement[i] = complements['C']
    elif complement[i] == 'G':
        complement[i] = complements['G']
    elif complement[i] == 'T':
        complement[i] = complements['T']

k_length = [4, 5, 6, 7, 8, 9, 10, 11, 12]

results = {'positions': [], 'length': []}

for k in k_length:
    for i in range(0, len(dna)-k+1):
        sub1 = dna[i:i+k]
        sub2 = complement[i:i+k]
        sub2.reverse()
        if sub1 == sub2:
            results['positions'].append(i+1)
            results['length'].append(k)

df = pd.DataFrame(results).sort_values(by=['positions'])
