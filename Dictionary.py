d1 = {"r": "peter", "s": "Nutkin", "b": "Benjamin"}
print(d1)
print(d1["s"])

#c = d1["nokey"]
d1["k"] = "Tom"
print(d1)

del d1["r"]
print(d1)

#del d1["nokey"]
print(d1)

k1 = ("f", "m", "d")
print(k1)

v1 = {"Jeremy", "Moppet", "Jemima"}
print(v1)

d2 = dict(zip(k1, v1))
print(d2)

d3 = dict(r="Peter", m="Johnny")
print(d3)

print(len(d3))

print("r" in d3)

print("b" not in d3)
