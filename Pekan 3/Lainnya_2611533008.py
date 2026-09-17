print("================================")
print("1. OPERATOR KEANGGOTAAN")
print("================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3008 = input("Masukkan beberapa angka, pisahkan dengan koma): ")

# Mengubah input menjadi list integer
data_3008 = [int(angka.strip()) for angka in input_data_3008.split(",")]

nilai_dicari_3008 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3008 = nilai_dicari_3008 in data_3008
print("\nOperator keanggotaan IN")
print(nilai_dicari_3008, "in", data_3008, "=", hasil_3008)

# Operator not in
hasil_3008 = nilai_dicari_3008 not in data_3008
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3008, "not in", data_3008, "=", hasil_3008)

print("\n==============================")
print("2. OPERATOR IDENTITAS")
print("==============================")

# objek1 menggunakan list dari input pengguna
objek1_3008 = data_3008

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3008 = objek1_3008

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3008 = data_3008.copy()

print("objek1_3008", objek1_3008)
print("objek2_3008", objek2_3008)
print("objek3_3008", objek3_3008)

# Operator is
hasil_3008= objek1_3008 is objek2_3008
print("\nOperator identitas IS")
print("objek1_3008 is objek2_3008", hasil_3008)

# Operator is not
hasil_3008 = objek1_3008 is not objek3_3008
print("\nOperator  IS NOT")
print("objek1_3008 is not objek3_3008", hasil_3008)

# Membandingkan identitas dengan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_3008 is objek3_3008", objek1_3008 is objek3_3008)
print("objek2_3008 == objek3_3008", objek2_3008 == objek3_3008)








