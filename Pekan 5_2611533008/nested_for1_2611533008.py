batas_3008 = int(input("masukkan nilai batas: "))
for line in range (1, batas_3008 + 1):
    for j in range(1, (-1*line + batas_3008 + 1)):
        print(".", end="")
    print(line)