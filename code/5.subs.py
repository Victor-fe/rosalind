st = 'GATATATGCATATACTT'
sub = 'ATAT'

positions = []

for i in range(0, len(st)):
    if st[i:i+4] == sub:
        positions.append(i+1)
