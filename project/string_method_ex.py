#validate user input interface
# 1. username is nor more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("masukkan username: ")

if len(username) > 12:
    print("username tidak boleh lebih dari 12 karakter")
elif not username.find(" ") == -1:
    print("username tidak boleh mengandung spasi")
elif not username.isalpha():
    print("username tidak boleh mengandung angka")
else:
    print(f"selamat datang. {username}")