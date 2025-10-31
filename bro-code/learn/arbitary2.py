# *args = membolehkan membuat multiple non-key arguments
# **kwargs = membolehkan membuat multiple keywords arguments

#args
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    # print()
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr", "Raihan", "Kamil", "list",
                street="123 gang palsu",
                apt="100",
                city="bandung",
                state="Jabar",
                zip="54321")
