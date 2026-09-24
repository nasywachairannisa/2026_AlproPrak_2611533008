# program menghitug diskon belanja

# input dari user
total_belanja_3008 = float(input("Masukkan total belanja (Rp): "))

# input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3008 = input("apakah anda member? (y/t): "). strip() .lower() 
is_member_3008 = input_member_3008 in ["y", "ya"]

# input status kode promo ( mengecek apakah user mengeti 'y atau 'ya')
input_promo_3008 = input("apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3008 = input_promo_3008 in [ "y", "ya"]

total_diskon_persen_3008 = 0

# multi -  IF terpisah : setiap kondisi diperiksa secara independen
# diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3008 > 1000000:
    total_diskon_persen_3008 += 10 # diskon belanja besar
    
if is_member_3008:
    total_diskon_persen_3008 += 5 # diskon member
    
if kode_promo_valid_3008:
    total_diskon_persen_3008 += 15 # diskon voucher
    
# menghitung nominal diskon dan total bayar
nominal_diskon_3008 = total_belanja_3008 * (total_diskon_persen_3008 / 100)
total_bayar_3008 =  total_belanja_3008 - nominal_diskon_3008

# output hasil

print("\n --- RINCIAN PEMBAYARAN ---")
print (f"Total diskon  : {total_diskon_persen_3008}% (Rp {nominal_diskon_3008:,.0f})")
print(f"Total bayar  : {total_bayar_3008:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3008}%")

# output: total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid


