
print("\n----SISTEM LOKET ALPRO ADVENTURE PARK---")

# input data pengunjung
    
nama_pengunjung_3008 = (input("Masukkan nama anda: "))
umur_pengunjung_3008 = int(input("Masukkan umur anda: "))
kepemilikan_simC_3008 = (input("Apakah memiliki sim C (y/t)?: "))[0].strip().lower()

# pemilihan wahana menggunakan match

(print("\nPilihan paket wahana (1-5)"))
print("""  
1. Safari Rimba        (Rp 50,000)
2. Arung Jeram          (Rp 75,000)
3. Motor ATV Ekstrim    (Rp 120,000)
4. Roller Coaster Kilat (Rp 100,000)
5. All-Access VIP       (Rp 220,000)
""")

pilihan_wahana_3008 = int(input("Masukkan nomor paket (1-5): "))
jumlah_tiket_3008 = int(input("Masukkan jumlah tiket: "))
member_3008 = (input("Apakah anda member? (y/t): ")) [0].strip().lower()
kode_promo_3008 = input("Apakah kode promo valid? (y/t): ") [0].strip().lower()


match pilihan_wahana_3008:
    case 1:
        nama_wahana_3008 = "Safari Rimba"
        harga_3008 = 50000
    case 2:
        nama_wahana_3008 = "Arung Jeram"
        harga_3008 = 75000
    case 3:
        nama_wahana_3008 = "Motor ATV Ekstrim"
        harga_3008 = 120000
    case 4:
        nama_wahana_3008 = "Roller Coaster Kilat"
        harga_3008 = 100000
    case 5:
        nama_wahana_3008 = "All-Access VIP"
        harga_3008 = 220000
    case _:
        print("Pilihan tidak valid")
        raise SystemExit
    
if jumlah_tiket_3008 <= 0:
    print("Peringatan: Kuota tiket tidak valid")

# Validasi Izin Kendali Wahana Menggunakan if - elif - else dan Operator Logika (and, !=)

print(" \n---KELAYAKAN PENGENDARA WAHANA---")

if pilihan_wahana_3008 == 3 and umur_pengunjung_3008 >= 17 and kepemilikan_simC_3008 == 'y':
        print("\nStatus akses: Anda sudah dewasa dan boleh mengendarai ATV")

elif  pilihan_wahana_3008 == 3 and umur_pengunjung_3008 >= 17 and kepemilikan_simC_3008 != 'y':
    print("\nStatus akses: Anda sudah dewasa tetapi tidak boleh mengendarai ATV (wajib didampingi instruktur)")
    
elif  pilihan_wahana_3008 == 3 and umur_pengunjung_3008 < 17 and kepemilikan_simC_3008 == 'y':
    print("\nStatus akses: identitas tidak valid. Belum cukup umur memiliki sim c")

elif pilihan_wahana_3008 == 3:
    print("\nStatus akses: Anda belum cukup umur dan tidak boleh bawa motor ATV")

elif pilihan_wahana_3008 != 3 and umur_pengunjung_3008 >= 10:
    print("\nStatus akses: Anda memenuhi batas usia wahana")
    
else:
    print("\nStatus akses: Anda belum memenuhi batas usia wahana")
    


# Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah

subtotal_3008 = harga_3008 * jumlah_tiket_3008
total_diskon_3008 = 0
if subtotal_3008 >= 200000:
    total_diskon_3008 += 10 # Diskon belanja besar

if member_3008 in ['y','ya']:  # diskon member
    total_diskon_3008 += 5

if kode_promo_3008 in ['y', 'ya']:  # diskon voucher promo
    total_diskon_3008 += 15

if jumlah_tiket_3008 >= 5: 
    total_diskon_3008 += 5 # diskon tambahan rombongan

nominal_diskon_3008 = subtotal_3008 * (total_diskon_3008 / 100)
total_bayar_3008 = subtotal_3008 - nominal_diskon_3008

print(" \n---RINCIAN PEMBAYARAN---")

print (f"\nSubtotal belanja: {subtotal_3008:,.0f}")
print (f"\nTotal diskon: {total_diskon_3008:,.0f}%,(Rp.{nominal_diskon_3008: ,.0f})")
print(f"\nTotal bayar: {total_bayar_3008:,.0f}")

if total_bayar_3008 > 300000:
    
    print("\nCatatan Layanan: Selamat! Anda berhak mendapatkan Souvenir Gratis")
else:
    print("\nCatatan Layanan: Terima Kasih telah berkunjung")
print("\nProgram selesai")