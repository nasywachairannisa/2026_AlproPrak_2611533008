umur_3008 = int(input(" Masukkan umur anda: "))
sim_3008 = input("Apakah anda punya sim (y/t): ") [0]

if umur_3008 >= 17 and sim_3008 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3008 >= 17 and sim_3008 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3008 < 17 and sim_3008 == 'y' :
    print("Anda belum cukup umur punya sim")

if umur_3008 < 17 and sim_3008 != 'y':
    print("Anda belum cukup umur bawa motor")


    