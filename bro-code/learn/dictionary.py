# dictionary {key:value} ordered dan bisa dirubah, no duplicates

capitals = {"USA":"Washinton DC",
            "India":"New Delhi",
            "China":"Beijing", 
            "Rusia":"Moscow"}

if capitals.get("Japan"):
    print("That capital exist")
else:
    print("That capital doesnt exist")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"LA"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# keys = capitals.keys()
# values = capitals.values()
items = capitals.items()


print(items)