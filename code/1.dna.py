dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in dna:
    if i == 'A':
        counts['A'] += 1
    elif i == 'C':
        counts['C'] += 1
    elif i == 'G':
        counts['G'] += 1
    elif i == 'T':
        counts['T'] += 1
