strings = {
    'Rosalind_52': 'TCATC',
    'Rosalind_44': 'TTCAT',
    'Rosalind_68': 'TCATC',
    'Rosalind_28': 'TGAAA',
    'Rosalind_95': 'GAGGA',
    'Rosalind_66': 'TTTCA',
    'Rosalind_33': 'ATCAA',
    'Rosalind_21': 'TTGAT',
    'Rosalind_18': 'TTTCC'
}

strings_1 = []
for s in strings:
    for t in strings:
        print(strings[s], strings[t], s, t)
        error = 0
        for i in range(len(strings[s])):
            if strings[s][i] != strings[t][i]:
                error += 1
        if error == 1:
            strings_1.append([strings[s], strings[t]])

for pair in strings_1:
    pair.sort()

unique_data = [list(x) for x in set(tuple(x) for x in strings_1)]
