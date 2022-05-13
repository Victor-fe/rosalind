strings = {
    'Rosalind_14': 'ACGTACGTGACG',
    'Rosalind_18': 'GTA'
}

string = strings['Rosalind_14']
pattern = strings['Rosalind_18']
positions = []
start = 0
for p in range(len(pattern)):
    for s in range(start, len(string)):
        if pattern[p] == string[s]:
            start = s+2
            positions.append(s+1)
            break

