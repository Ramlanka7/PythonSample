import sys

a = 0

for k in sys.modules:
    a = a + 1

print(a)

print(len(sys.modules))

y = 4
z = 12
x = 3 < y < z < 10
s = not 3 < y < z < 10
print(x)
print(s)
