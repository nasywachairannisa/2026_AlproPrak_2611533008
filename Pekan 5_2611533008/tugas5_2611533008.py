n_3008 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border atas
print("#", end="")

for i_3008 in range(4 * n_3008 + 5):
    print("=", end="")

print("#")


# jam pasir atas
for baris_3008 in range(n_3008, 0, -1):

    print("| ", end="")

    for spasi_3008 in range(2 * (n_3008 - baris_3008)):
        print(" ", end="")

    for angka_3008 in range(baris_3008, 0, -1):
        print(angka_3008, end=" ")

    print("<*>", end="")

    for angka_3008 in range(1, baris_3008 + 1):
        print(" ", end="")
        print(angka_3008, end="")
        
    for spasi_3008 in range(2 * (n_3008 - baris_3008)):
        print(" ", end="")

    print(" |")


# poros titik pusat
print("|", end="")

for spasi_3008 in range(2 * n_3008 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_3008 in range(2 * n_3008 + 1):
    print(" ", end="")

print("|")


# jam pasir bawah
for baris_3008 in range(1, n_3008 + 1):

    print("| ", end="")

    for spasi_3008 in range(2 * (n_3008 - baris_3008)):
        print(" ", end="")

    for angka_3008 in range(baris_3008, 0, -1):
        print(angka_3008, end=" ")

    print("<*>", end="")

    for angka_3008 in range(1, baris_3008 + 1):
        print(" ", end="")
        print(angka_3008, end="")

    for spasi_3008 in range(2 * (n_3008 - baris_3008)):
        print(" ", end="")

    print(" |")


# Border bawah
print("#", end="")

for i_3008 in range(4 * n_3008 + 5):
    print("=", end="")

print("#")