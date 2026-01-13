import base64
choice = input("Type 'e' to encode or 'd' to decode: ").lower()
name = input("Enter a string to encode/decode with Base64: ")

if choice == 'e':
    encoded_bytes = base64.b64encode(name.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    print(f"Encoded string: {encoded_str}")

elif choice == 'd':
    decoded_bytes = base64.b64decode(name)
    decoded_str = decoded_bytes.decode('utf-8')
    print(f"Decoded string: {decoded_str}")
