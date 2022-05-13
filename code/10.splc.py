table = {
    'UUU': 'F',
    'UUC': 'F',
    'UUA': 'L',
    'UUG': 'L',
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'AUG': 'M',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'UAU': 'Y',
    'UAC': 'Y',
    'UAA': 'Stop',
    'UAG': 'Stop',
    'CAU': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'AAU': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'UGU': 'C',
    'UGC': 'C',
    'UGA': 'Stop',
    'UGG': 'W',
    'CGU': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'AGU': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G'
}

strings = {
    'Rosalind_10': 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG',
    'Rosalind_12': 'ATCGGTCGAA',
    'Rosalind_15': 'ATCGGTCGAGCGTGT'
}

dna = strings['Rosalind_10']
introns = [strings['Rosalind_12'], strings['Rosalind_15']]

for intron in introns:
    dna = dna.replace(intron, '')

rna = dna.replace('T', 'U')

protein = []

for start in range(0, len(rna)):
    if rna[start:start+3] == 'AUG':
        for i in range(start, len(rna), 3):
            if table[rna[i:i + 3]] == 'Stop':
                break
            protein.append(table[rna[i:i + 3]])
        break

protein = ''.join(protein)
