pin = input("Enter PIN: ")
attempt = 1
MAX_ATTEMPTS = 3
correct_pin = "1234"

while pin != correct_pin and attempt < MAX_ATTEMPTS:
    attempt += 1
    print("Incorrect PIN.")
    pin = input("Enter PIN: ")
    
if pin == correct_pin:
    print("Access granted")
else:
    print("Account locked")