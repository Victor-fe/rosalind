strings = {
    'Rosalind_23': 'AACCTTGG',
    'Rosalind_64': 'ACACTGTGA'
}

motif = ''
start = 0

for i in range(len(strings['Rosalind_23'])):
    print('loop_1', strings['Rosalind_23'][i], i)
    for j in range(start, len(strings['Rosalind_64'])):
        print('loop_2', strings['Rosalind_64'][j], j)
        if strings['Rosalind_23'][i] == strings['Rosalind_64'][j]:
            motif += strings['Rosalind_23'][i]
            start = j + 1
            break
