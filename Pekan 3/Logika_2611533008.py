# Memasukkan nilai boolean
# input tidak peka terhadap huruf besar dan kecil
a1_3008 = input("Input nilai boolean-1 (true/false):"). strip().lower() == "true"
a2_3008 = input("Input nilai boolean-2 (true/false):"). strip().lower() == "true"

print("\n A1_3008 =", a1_3008)
print("A2_3008 =", a2_3008)

# Konjungsi: bernilai True jika keduanya true
hasil_3008 = a1_3008 and a2_3008
print("\nKonjungsi (AND)")
print("A1_3008 and A2_3008 =", hasil_3008)

# Disjungsi : bernilai True jika salah satunya true
hasil_3008 = a1_3008 or a2_3008 
print("\nDisjungsi (OR)")
print("A1_3008 or A2_3008 = ", hasil_3008)

# Negasi A1 : membalik nilai A1
hasil_3008 = not a1_3008
print("\nNegasi A1 (NOT)")
print("not A1_3008 =", hasil_3008)

# Negasi A2 : membalik nilai A2
hasil_3008 = not a2_3008
print("\nNegasi A2 (NOT)")
print("not A2_3008 =", hasil_3008)

#XOR : bernilai true jika kedua nilai berbeda
hasil_3008 = a1_3008 != a2_3008
print("\nDisjungsi ekslusif (XOR)")
print("A1_3008 XOR A2_3008 =", hasil_3008)