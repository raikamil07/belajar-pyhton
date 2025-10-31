# def happy_birthday(name):
#     print(f"happy birhday to {name}")
#     print("You are old")
#     print("happy birhday to you")
#     print()

# nama = ["raihan", "steve", "job"]

# for i in range(1):
#     for n in nama:
#         happy_birthday(n)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"this is the bill amount ${amount:.2f} is due to {due_date}")
    print("please pay it")

display_invoice("raihan", 45.01, "19/8/2025")