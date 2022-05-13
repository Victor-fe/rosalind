dna = 'AAAACCCGGT'
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

complement.reverse()

revc = ''.join(complement)
