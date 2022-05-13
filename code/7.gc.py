strings = {
    'Rosalind_6404': 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG',
    'Rosalind_5959': 'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
    'Rosalind_0808': 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
}

strings_content = {}
for i in strings:
    counts = 0
    for j in strings[i]:
        if j == 'C' or j == 'G':
            counts += 1
    nchar = len(strings[i])
    content = (counts / nchar) * 100
    temp = {i: content}
    strings_content.update(temp)

label_max = max(strings_content, key=strings_content.get)
content_max = strings_content[label_max]

print(label_max)
print(content_max)
