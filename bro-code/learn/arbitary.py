# *args = membolehkan membuat multiple non-key arguments
# **kwargs = membolehkan membuat multiple keywords arguments

#args
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total    

print(add(1,2,3,4,5))

#kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(print_address(street="pagarsih", 
                    city="bandung", 
                    state="jawa barat", 
                    zip=12345))