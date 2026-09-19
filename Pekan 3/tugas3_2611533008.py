print("\n==============================")
print("SISTEM TRANSAKSI TOKO")
print("==============================")


# Sistem Transaksi

nama_3008 = (input("Masukkan nama pelangan:"))
status_pelanggan_3008 = (input ("Apakah member? "))
total_belanja_3008 = (float(input("Masukkan total belanja:")))
jumlah_belanja_3008 = (int(input("Masukkan banyak barang belanjaan:")))
promo_3008 = (input("Masukkan kode promo: "))
kode_promo_3008 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# Data Transaksi

print("\n==============================")
print("DATA PELANGGAN DAN TRANSAKSI")
print("==============================")

print("\nNama Pelanggan: ", nama_3008)
print("\nStatus Pelanggan:", status_pelanggan_3008)
print("\nTotal Belanja: ", total_belanja_3008)
print("\nJumlah Barang: ", jumlah_belanja_3008)
print("\nKode promo: ", promo_3008)

# HASIL VALIDASI

print("\n==============================")
print("HASIL VALIDASI")
print("==============================")

banyak_belanja_3008 = total_belanja_3008 >= 200000
jumlah_barang_3008 = jumlah_belanja_3008 >= 3
status_member_3008 = status_pelanggan_3008 == "member"
hasil_promo_3008 = promo_3008 in kode_promo_3008 
dapat_diskon_3008 = status_member_3008 and banyak_belanja_3008
dapat_promo_3008  = jumlah_barang_3008 and hasil_promo_3008

print("\nBelanja >= 200000: ", banyak_belanja_3008)
print("\nJumlah barang >= 3: ", jumlah_barang_3008)
print("\nStatus member: ", status_member_3008)
print("\nKode promo tersedia: ", hasil_promo_3008)
print("\nMendapakan diskon: ", dapat_diskon_3008)
print("\nMendapatkan promo: ", dapat_promo_3008)

# HASIL PERHITUNGAN

print("\n==============================")
print("HASIL PERHITUNGAN")
print("==============================")

# diskon member = 10%
if status_member_3008 and banyak_belanja_3008:
    diskon_3008 = total_belanja_3008 * 10 / 100
else:
    diskon_3008 = 0
    
total_pembayaran_3008 = total_belanja_3008 
total_pembayaran_3008 -= diskon_3008

rata_harga_3008 = total_pembayaran_3008 / jumlah_belanja_3008

print("\nDiskon: ", diskon_3008)
print("\nTotal Pembayaran: ", total_pembayaran_3008)
print("\nRata-rata harga: ", rata_harga_3008)


# OPERATOR IDENTITY

print("\n==============================")
print("OPERATOR IDENTITY")
print("==============================")

objek_a_3008 = kode_promo_3008
objek_b_3008 = kode_promo_3008
objek_c_3008 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

print("\nA is B:", objek_a_3008 is objek_b_3008)
print("A is not C:", objek_a_3008 is not objek_c_3008)


# HAK AKSES PELANGGAN

# 0001 = Pelanggan merupakan member
# 0010 = Total belanja ≥ Rp200.000
# 0100 = Jumlah barang ≥ 3
# 1000 = Kode promo tersedia

print("\n==============================")
print("HAK AKSES PELANGGAN")
print("==============================")

member_akses_3008 = status_member_3008 
promo_akses_3008 = dapat_promo_3008
freeshipping_akses_3008 = promo_3008 == "GRATISONGKIR"

kode_hak_akses_3008 = 0

if member_akses_3008:
    kode_hak_akses_3008 = kode_hak_akses_3008 | 1

if promo_akses_3008:
    kode_hak_akses_3008 = kode_hak_akses_3008 | 2

if freeshipping_akses_3008:
    kode_hak_akses_3008 = kode_hak_akses_3008 | 4
    
print("\nKode hak akses: ", kode_hak_akses_3008)
print("\nMember akses: ", member_akses_3008)
print("\nPromo akses: ", promo_akses_3008)
print("\nFreeshipping akses: ", freeshipping_akses_3008)
    

# OPERASI BITWISE
# Nilai bit:
# 0001 = Member
# 0010 = Belanja >= 200000
# 0100 = Jumlah barang >= 3
# 1000 = Promo tersedia

kode_status_3008 = 0
if status_member_3008:
    kode_status_3008 = kode_status_3008 | 1
    
if banyak_belanja_3008:
    kode_status_3008 = kode_status_3008 | 2
    
if jumlah_barang_3008:
    kode_status_3008 = kode_status_3008 | 4

if dapat_promo_3008:
    kode_status_3008 = kode_status_3008 | 8

print("\n==============================")
print("Kode Status Transaksi")
print("==============================")

print("\n 0001 | 0010 | 0100 | 1000")
print("\nKode biner: ", format(kode_status_3008, "04b"))
print("\nKode desimal: ", kode_status_3008)

print("\n==============================")
print("PEMERIKSAAN STATUS")
print("==============================")

print("\nCek member")
print(format(kode_status_3008, "04b"), "& 0001")

cek_member_3008 = kode_status_3008 & 1
print("\nHasil biner: ", format(cek_member_3008, "04b"))
print("\nHasil desimal: ", cek_member_3008)

print("\nCek promo")
print(format(kode_status_3008, "04b"), "& 1000")

cek_promo_3008 = kode_status_3008 & 8
print("\nHasil biner: ", format(cek_promo_3008, "04b"))
print("\nHasil desimal: ", cek_promo_3008)


print("\n==============================")
print("PERBANDINGAN STATUS")
print("==============================")

kode_transaksi_3008 = kode_status_3008
kode_referensi_3008 = 11

print("\nKode transaksi: ", format(kode_transaksi_3008, "04b"))
print("\nKode referensi: ", format(kode_referensi_3008, "04b"))

hasil_xor_3008 = kode_transaksi_3008 ^ kode_referensi_3008

print("\n" + format(kode_transaksi_3008,"04b"), "^", format(kode_referensi_3008,"04b"))
print("\nHasil biner: ", format(hasil_xor_3008, "04b"))
print("\nHasil desimal: ", hasil_xor_3008)

print("\n==============================")
print("KODE SHIFT")
print("==============================")

kode_shift_3008 = kode_status_3008 << 1

print("\n" + format(kode_status_3008, "04b"), "<<", "1")
print("\nHasil biner: ", format(kode_shift_3008, "04b"))
print("\nHasil desimal: ", kode_shift_3008)


print("\n==============================")
print("SELESAI")
print("==============================")



