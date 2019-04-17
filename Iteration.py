for q in [1, 2, 3, 4]:
    print(q)

r = {'a': 1, 'b': 2, 'c': 3}
for q in r:
    print("key:", q, 'value:', r[q])

for q in range(0, 5, 2):
    print(q)

for index, value in enumerate('ab', 1):
    print("At index", index, "Value", value)

a = [x for x in range(5)]

b = [0]

for q in range(5):
    b.append(q)

print(a)
print(b)
print('That\'s all folks')

a = [x for x in range(5) if x % 2]
b = []

for q in range(5):
    if q % 2:
        b.append(q)

print(a)
print(b)
print('That\'s all folks')
