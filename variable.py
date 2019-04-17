a = 'Nice ' "Dragon"
b = "Nice " + 'Dragon'
c = """Nice Dragon"""
d = '''Nice Dragon'''
print(a == b)
print(a == c)
print(a is b)
print(a is c)
print(a.__gt__(b))

eggs = '{0} and {1}'.format('spam', 'eggs')
print(eggs)


