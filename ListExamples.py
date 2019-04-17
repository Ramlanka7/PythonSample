q = [1, "Plum", 3.14, 2, "One", 3]

print(q[1])

print(q[0:2])

print(q[1:])

print(q[-1])

print(q[:3])

a = [1, 2, 3]
b = [4, 5, 6]

print(a * 2)

c = a + b
print(c)

del c[1:3]
print(c)

d = [1, 2, 3, 4, 5, 6]
d[1] = 'a'
print(d)

d[2:4] = ['b', 'c']
print(d)

d[2:4] = ["A", "B", "C", "D"]
print(d)
