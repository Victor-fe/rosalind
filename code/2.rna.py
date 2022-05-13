dna = 'GATGGAACTTGACTACGTAAATT'
rna = list(dna)

for i in range(0, len(rna)):
    if rna[i] == 'T':
        rna[i] = 'U'

rna = ''.join(rna)
