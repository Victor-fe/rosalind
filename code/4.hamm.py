st1 = 'GAGCCTACTAACGGGAT'
st2 = 'CATCGTAATGACGGCCT'

count = 0

for i in range(0, len(st1)):
    if st1[i] != st2[i]:
        count += 1
