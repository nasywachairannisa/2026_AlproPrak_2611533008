angka1_3008 = int(input("input angka-1:"))
angka2_3008 = int(input("input angka-2:"))

print("\nNilai awal angka1_3008 =", angka1_3008)
print("Nilai awal angka2_3008 =", angka2_3008)

# Assignment biasa (=)
hasil_3008 = angka1_3008
print("\nAssignment biasa (=)")
print("hasil =", hasil_3008)

# Assignment penambahan (+=)
hasil_3008 = angka1_3008
hasil_3008 += angka2_3008
print ("\nAssignment penambahan (+=)")
print("hasil =", hasil_3008)

# Assignment pengurangan (-=)
hasil_3008 = angka1_3008
hasil_3008 -= angka2_3008
print("\nAssignment pengurangan (-=)")
print("hasil =", hasil_3008)

# Assignment perkalian (*=)
hasil_3008 = angka1_3008
hasil_3008 *= angka2_3008
print("\nAssignment perkalian (*=)")
print("hasil =", hasil_3008)

# Assigment pembagian, pembagian bulat , dan sisa bagi (/=, //=, %=)
if angka2_3008 !=0:
    hasil_3008 = angka1_3008
    hasil_3008 /= angka2_3008
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil_3008)
    
    # Operator tambahan
    hasil_3008 = angka1_3008
    hasil_3008 //= angka2_3008
    print("\nAssignment pembagian bulat (//=)")
    print("hasil =", hasil_3008)
    
    hasil_3008 = angka1_3008
    hasil_3008 %= angka2_3008
    print("\nAssignment sisa bagi (%=)")
    print("hasil =", hasil_3008)
else: 
    print("\nPembagian tidak dapat dilakukan")
    print("angka kedua tidak boleh bernilai 0")
    
# Operator tambahan : assigment perpangkatan (**=)
hasil_3008 =  angka1_3008
hasil_3008 **= angka2_3008
print("\nAssignment perpangkatan (**=)")
print("hasil =", hasil_3008)






