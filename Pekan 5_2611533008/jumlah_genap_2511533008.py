ulang_3008 = int(input("masukkan nilai batas: " ))

jumlah_3008 = 0
for i in range(1, ulang_3008 + 1):
    if i % 2 == 0:
        print(i, end="")
        jumlah_3008 = jumlah_3008 + i

        if i < ulang_3008:
            print("+", end="")

        else:
            print("=", jumlah_3008, end="")
print()
print("jumlah = ", jumlah_3008)
