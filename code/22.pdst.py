strings = ['TTTCCATTTA', 'GATTCATTTC', 'TTTCCATTTT', 'GTTCCATTTA']

matrix = []

for first in strings:
    matrix_sub = []
    for second in strings:
        mismatches = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                mismatches += 1
        distance = mismatches / len(first)
        matrix_sub.append(distance)
    matrix.append(matrix_sub)
