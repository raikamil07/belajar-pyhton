# or = setidaknya satu kondisi harus benar
# and = semua kondisi harus benar
# not = membalik nilai boolean

# temp = 35
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("the outdoor event is cancelled")
# else:
#     print("the outdoor event is still scheduled")

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("it is hot and sunny")
elif temp <= 0 and is_sunny:
    print("it is cold and sunny")
elif 28 > temp > 0 and is_sunny:
    print("the warm outside and sunny")
elif temp >= 28 and not is_sunny:
    print("it is hot and cloudy")
elif temp <= 0 and not is_sunny:
    print("it is cold and cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("the warm outside and cloudy") 