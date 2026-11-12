# A
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")

elif not username.isalnum():
    print("Invalid: letters and digits only")

elif not username[0].isalpha():
    print("Invalid: must start with a letter")

else:
    print("Valid")

# B

nim = input("masukkan NIM: ")

if len(nim) != 10 or not nim.isdigit():
    print("Invalid NIM")
else:
    print("Valid, intake year 20" + nim[:2])
