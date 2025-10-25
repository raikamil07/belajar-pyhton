foods = []
prices = []
total = 0

while True:
    food = input("enter food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("enter price of the food: $"))
        foods.append(food)
        prices.append(price)

print(" -- Shopping Cart ---")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Total price: ${total}")