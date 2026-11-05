total = 0

while True:
    number = int(input("masukkan number: "))

    if number < 0:
        break
    if number == 0:
        continue

    print("positive number:", number)
    total += number

print("Total:", total)