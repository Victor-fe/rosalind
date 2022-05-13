import json
import os

os.chdir("/Users/v/Documents/rosalind")
dna_prot = json.load(open("dna_prot.json"))
dna_dna = json.load(open("dna_dna.json"))

dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

temp = []
for i in dna:
    temp.append(dna_dna[i])

temp.reverse()
temp = ''.join(temp)

strings = [dna, temp]

orf = set()
for string in strings:
    print(string)
    for index in range(len(string)-2):
        print(index)
        if string[index:index+3] == 'ATG':
            print('START')
            protein = ''
            codon = index
            while codon+3 < len(string)-1:
                if dna_prot[string[codon:codon + 3]] == 'Stop':
                    orf.add(protein)
                    break
                else:
                    protein += dna_prot[string[codon:codon + 3]]
                    codon += 3
