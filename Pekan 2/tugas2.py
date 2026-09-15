from typing import Final

# Konstanta batas kelulusan
BATAS_LULUS: Final[float] = 75.0

# Mengambil data dari praktikan
nama_3008 = input("Masukkan nama praktikan: ")
umur_3008 = int(input("Masukkan umur: "))
semester_3008 = int(input("Masukkan semester: "))
inisial_3008 = input("Masukkan inisial: ")
jenis_kelamin_3008 = input("Masukkan jenis kelamin (L/P): ")

alamat_3008 = """ 
    Kampus Unand
    Kec.pauh
    Kota Padang
"""""

nilai_3008 = float(input("Masukkan nilai tes awal: "))

# Token identifikasi menggunakan bilangan kompleks
token_3008 = 100 + 3j

# Verifikasi kelulusan
lulus_3008 = nilai_3008 >= BATAS_LULUS

# Menampilkan hasil
print("\n===== DATA PRAKTIKAN =====")

print("Nama           :", nama_3008)
print("Tipe data      :", type(nama_3008))

print("Umur           :", umur_3008)
print("Tipe data      :", type(umur_3008))

print("Semester       :", semester_3008)
print("Tipe data      :", type(semester_3008))

print("Inisial        :", inisial_3008)
print("Tipe data      :", type(inisial_3008))

print("Jenis Kelamin  :", jenis_kelamin_3008)
print("Tipe data      :", type(jenis_kelamin_3008))

print("Alamat         :", alamat_3008)
print("Tipe data      :", type(alamat_3008))

print("Nilai Tes      :", nilai_3008)
print("Tipe data      :", type(nilai_3008))

print("Token          :", token_3008)
print("Tipe data      :", type(token_3008))

print("Batas Lulus    :", BATAS_LULUS)
print("Tipe data      :", type(BATAS_LULUS))

print("Status Lulus   :", lulus_3008)
print("Tipe data      :", type(lulus_3008))