strings = {
    'Rosalind_0209': 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT',
    'Rosalind_2200': 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
}

strings = list(strings.values())
base_type = {'A': 'purine', 'C': 'pyrimidine', 'G': 'purine', 'T': 'pyrimidine'}
transition = 0
transversion = 0

for i in range(len(strings[0])):
    if strings[0][i] == strings[1][i]:
        pass
    elif base_type[strings[0][i]] == base_type[strings[1][i]]:
        transition += 1
    elif base_type[strings[0][i]] != base_type[strings[1][i]]:
        transversion += 1

ratio = transition/transversion
