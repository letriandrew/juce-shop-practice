name = input("Enter a string to encode/decode with ROT13: ")

for i in name:
    if 'a' <= i <= 'z':
        offset = ord('a')
        print(chr((ord(i) - offset + 13) % 26 + offset), end='')
    elif 'A' <= i <= 'Z':
        offset = ord('A')
        print(chr((ord(i) - offset + 13) % 26 + offset), end='')
    else:
        print(i, end='')