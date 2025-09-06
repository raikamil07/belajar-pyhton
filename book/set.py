s = set([10,20,30,40,40,50])

print(s)

print("setelah di add")

s.add(60)

print(s)

print("setelah di update")

s.update([90,100,110])

print(s)

print("setelah di remove")

s.remove(20)

print(s)

print("setelah di clear")

s.clear()

print(s)

s = frozenset([19,29,39,49,59,69,79,89,99])

print("frozen set tidak dapat dilakukan perubahan" + str(s))