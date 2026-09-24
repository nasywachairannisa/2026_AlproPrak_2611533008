umur_3008 = int(input("Input umur anda: "))
sim_3008 = input("Apakah anda sudah punya sim c:") [0]

if umur_3008 >= 17 and sim_3008 == 'y':
    print ("Anda sudah dewasa dan boleh bawa motor ")

elif umur_3008 >= 17 and sim_3008 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

elif umur_3008 < 17 and sim_3008 == 'y':
    print("anda belum cukup umur punya sim")
    
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")

print("Program selesai")




