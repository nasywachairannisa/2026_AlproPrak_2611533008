is_lulus_3008 = True
is_cumlaude_3008 = True

nilai_3008 = 85
batas_lulus_3008 = 75

status_kelulusan_3008 = nilai_3008 >= batas_lulus_3008 

print("==== Check Kelulusan ====")
print("nilai:", nilai_3008)
print("Apakah lulus:", status_kelulusan_3008)
if is_lulus_3008 and is_cumlaude_3008:
    print("Selamat, Anda lulus dengan predikat Cum Laude")