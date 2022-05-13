import itertools

bases = ['A', 'C', 'G', 'T']
n = 2

kmers = [''.join(item) for item in itertools.product(bases, repeat=n)]
