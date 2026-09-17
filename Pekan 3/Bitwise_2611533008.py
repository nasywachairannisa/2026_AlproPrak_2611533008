print("\n==============================")
print("3. OPERATOR BITWISE")
print("==============================")

angka1_3008 = int(input("masukkan angka bitwise-1:"))
angka2_3008 =  int(input("masukkan angka bitwise-2:"))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_3008 =", angka1_3008, "| biner =", bin(angka1_3008))
print("angka2_3008 =,", angka2_3008, "| biner =", bin(angka2_3008))

# Bitwise AND
hasil_3008 = angka1_3008 & angka2_3008
print("\nBitwise AND (&)")
print(angka1_3008, "&", angka2_3008, "=", hasil_3008)
print("biner hasil =", bin(hasil_3008))
print("biner hasil (8 bit)=", format(hasil_3008, "08b"))

# Bitwise OR
hasil_3008 = angka1_3008 | angka2_3008
print("\nBitwise OR (|)")
print(angka1_3008, "|", angka2_3008, "=", hasil_3008)
print("Biner hasil =", bin(hasil_3008))
print("Biner hasil (8 bit) =", format(hasil_3008, "08b"))

# Bitwise XOR
hasil_3008 = angka1_3008 ^ angka2_3008
print("\nBitwise XOR (^)")
print(angka1_3008, "^", angka2_3008, "=", hasil_3008)
print("Biner hasil =", bin(hasil_3008))
print("Biner hasil (8 bit) =", format(hasil_3008, "08b"))

# Bitwise NOT
hasil_3008 = ~angka1_3008
print("\nBitwise NOT (~)")
print("~", angka1_3008, "=", hasil_3008)
print("Biner hasil =", bin(hasil_3008))
print("Biner hasil (8 bit) =", format(hasil_3008, "08b"))

# Bitwise geser kiri
jumlah_geser_3008 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3008 = angka1_3008 << jumlah_geser_3008
print("\nBitwise geser kiri (<<)")
print(angka1_3008, "<<", jumlah_geser_3008, "=", hasil_3008)
print("Biner hasil =", bin(hasil_3008))
print("Biner hasil (8 bit) =", format(hasil_3008, "08b"))

# Bitwise geser kanan
hasil_3008 = angka1_3008 >> jumlah_geser_3008
print("\nBitwise geser kanan (>>)")
print(angka1_3008, ">>", jumlah_geser_3008, "=", hasil_3008)
print("Biner hasil =", bin(hasil_3008))
print("Biner hasil (8 bit) =", format(hasil_3008, "08b"))
