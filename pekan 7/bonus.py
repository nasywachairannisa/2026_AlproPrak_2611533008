
kalimat = input("masukkan kalimat: ")

polindrom = kalimat.replace(" ", "").lower()

if polindrom == polindrom[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
