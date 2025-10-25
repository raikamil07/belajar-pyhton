x = set([1,2,3,4])

y = set([3,4,5,6])

a = x | y
b = x & y
c = x - y
d = x ^ y

print("Union:", a)
print("Intersection:", b)
print("Difference:", c)
print("Symmetric Difference:", d)