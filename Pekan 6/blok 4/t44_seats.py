blocked_seat = int(input("Masukkan blocked_seat: "))

for row in range(1, 4):
    print("Row", row, end=": ")
    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")
    print()