p = "Plum Lucky!"

# FOR
for i in p:
    print(i.upper())

print("That's all folks!")

# IF in FOR continue
for i in p:
    if i in 'aieou':
        continue
    print(i.upper())

print("That's all folks!")

# IF in FOR break
for i in p:
    if i in 'aieou':
        break
    print(i.upper())

print("That's all folks!")
