tinggi_3008 = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi_3008 + 1):
    for j in range(tinggi_3008 - i):
        print(" ", end="")
    
    for j in range(i):
        print("* ", end="")
    
    print()