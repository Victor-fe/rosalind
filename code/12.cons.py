from collections import Counter
import pandas as pd

strings = {
    'Rosalind_1': 'ATCCAGCT',
    'Rosalind_2': 'GGGCAACT',
    'Rosalind_3': 'ATGGATCT',
    'Rosalind_4': 'AAGCAACC',
    'Rosalind_5': 'TTGGAACT',
    'Rosalind_6': 'ATGCCATT',
    'Rosalind_7': 'ATGGCACT'
}

strings = list(strings.values())
scores = []
motif = ''
length = len(strings[0])

for i in range(length):
    bases = []
    for string in strings:
        bases.append(string[i])
    temp = Counter(bases)
    scores.append(temp)
    motif += max(temp, key=temp.get)

df = pd.DataFrame(scores).T.fillna(0)
df.sort_index(inplace=True)
