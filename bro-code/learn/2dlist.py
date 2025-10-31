# fruits = ["apples", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

groceries = [["apples", "orange", "banana", "coconut"],
            ["celery", "carrots", "potatoes"],
            ["chicken", "fish", "turkey"]]

# print(groceries[0][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()