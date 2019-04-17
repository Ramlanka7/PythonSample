import copy

a = [['this', 'is the', 'story'], [1234, 5678, 4538, 2340], ['uga-booga', 1234, 'hello']]

b = a[1][1]
print(b)

c = list(a)
d = c[1][1]
print(d)

e = copy.deepcopy(a)

print(a == e)

