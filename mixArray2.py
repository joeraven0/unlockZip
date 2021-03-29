from itertools import combinations

input = ['a', 'b', 'c', 'd']

output = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])

for x in output:
    print("".join(x))
