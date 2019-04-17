a = range(1, 8)
print(a)

range(1, 8)

for i in a:
    print(i)

b = range(7)
print(b)

b = list(range(7))
print(b)

b = list(range(1, 7, 2))
print(b)

c = range(7)
print(len(c))

print('a =', a)

a_10 = [x + 10 for x in a if x % 2 == 0]

print('a_10 =', a_10)
print("That's all folks!")
