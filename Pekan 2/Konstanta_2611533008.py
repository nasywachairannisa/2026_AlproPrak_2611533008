from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3008 = float(input('masukkan nilai jari-jari:'))
luas_3008 = PI * jari_3008 * jari_3008
print ("Luas lingkaran dengan jari-jari %.2f adalah %.2f" %(jari_3008, luas_3008))