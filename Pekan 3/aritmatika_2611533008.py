angka1_3008 = int(input("input angka-1:"))
angka2_3008 = int(input("input angka-2:"))

# Penjumlahan
hasil_3008 = angka1_3008 + angka2_3008
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3008)

# Pengurangan
hasil_3008 = angka1_3008 - angka2_3008
print("\nOperator Pengurangan")
print("Hasil =", hasil_3008)

# Perkalian'
hasil_3008 = angka1_3008 * angka2_3008
print("\nOperator Perkalian")
print("Hasil =", hasil_3008)

# Pembagian, pembagian bulat dan sisa bagi
if angka2_3008 != 0:
     hasil_3008 = angka1_3008 / angka2_3008
     print("\nOperator Pembagian")  
     print("Hasil =", hasil_3008)
     
     hasil_3008 = angka1_3008 // angka2_3008
     print("\nOperator pembagian bulat")
     print("Hasil =", hasil_3008)

     hasil_3008 = angka1_3008 % angka2_3008
     print("\nOperator sisa bagi")
     print("Hasil =", hasil_3008)
else:
    print("angka kedua tidak boleh bernilai 0")

# Pangkat
hasil_3008 = angka1_3008 ** angka2_3008
print("\nOperator pangkat")
print("Hasil =", hasil_3008)