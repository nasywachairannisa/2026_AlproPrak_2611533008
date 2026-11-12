# A
text = "Informatika"
print(text[10])
text = text.upper()
print(text)
print(text[0:20])

# B
text = "Nasywa Chairannisa"
text = text.lower()
count = 0
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)
