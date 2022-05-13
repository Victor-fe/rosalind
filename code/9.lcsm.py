strings = {
    'Rosalind_1': 'GATTACA',
    'Rosalind_2': 'TAGACCA',
    'Rosalind_3': 'ATACA'
}

strings_list = list(strings.values())

motifs = [min(strings_list, key=len)]
motif_len = len(motifs[0])

if len(set(motifs)) != 1:
    motif_len -= 1

motif_first = motifs[0]
lcsm = []

for length in range(motif_len, 1, -1):
    motifs_generated = []
    for i in range(0, len(motif_first) - length + 1):
        motifs_generated.append(motif_first[i:i + length])
    print('length', length)
    print('motifs_generated', motifs_generated)
    for motif in motifs_generated:
        hits_motif = []
        print('motif', motif)
        for string in strings_list:
            hits_in_string = []
            print('string', string)
            for i in range(0, len(string) - length + 1):
                sub = string[i:i + length]
                print('sub', sub)
                if sub == motif:
                    print('^^^')
                    hits_in_string.append(1)
                    hits_motif.append(1)
                    break
            if not hits_in_string:
                break
        if len(hits_motif) == len(strings_list):
            lcsm.append(motif)

