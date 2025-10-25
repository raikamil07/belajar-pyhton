item =  input("Enter the item name: ")
price = float(input("Enter the item price: "))
quantity = int(input("enter the item quantity: "))

total = price * quantity
print(f"the item you buy is {item}, you buy {quantity}pcs with the price {price} and total price is ${total}")