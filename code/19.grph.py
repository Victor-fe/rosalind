strings = {
    'Rosalind_0498': 'AAATAAA',
    'Rosalind_2391': 'AAATTTT',
    'Rosalind_2323': 'TTTTCCC',
    'Rosalind_0442': 'AAATCCC',
    'Rosalind_5013': 'GGGTGGG'
}

n = 3
overlap = []
for s in strings:
    for t in strings:
        if strings[s][-n:] == strings[t][:n] and s != t:
            print(strings[s][-n:], strings[t][:n], s, t)
            overlap.append([s, t])
