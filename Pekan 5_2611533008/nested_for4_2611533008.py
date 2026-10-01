tinggi_3008 = int(input("masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3008 % 2 != 0:
    print("tinggi harus bilangan genap")
else:
    a_3008 = tinggi_3008
    c_3008 = a_3008
    lebar_3008 = (2 * tinggi_3008) - 2

    for i in range(1, tinggi_3008 + 1):
        b_3008 = c_3008 + 1

        for j in range(1, lebar_3008 + 1):

            # baris atas dan bawah
            if i == 1 or i == tinggi_3008:
                if j == 1 or j == lebar_3008:
                    print("#", end="")
                else:
                    print("=", end="")

            # baris isi
            else:
                if j == 1 or j == lebar_3008:
                    print("|", end="")
                else:
                    if j == c_3008:
                        print("<", end="")
                    elif j == b_3008:
                        print(">", end="")
                    elif j == (lebar_3008 - c_3008):
                        print("<", end="")
                    elif j == (lebar_3008 - c_3008 + 1):
                        print(">", end="")
                    elif j > b_3008 and j < (lebar_3008 - c_3008):
                        print(".",end="")
                    else:
                        print(" ", end="")

        print()

        # logika asli java
        a_3008 -= 2
        
        if a_3008 <= 0:
            c_3008 = (-a_3008) + 2
        else:
            c_3008 = a_3008