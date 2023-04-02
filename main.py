binary_code = input("Enter binary code: ")
bytes_list = binary_code.split()

ascii_text = ""
for byte in bytes_list:
    decimal = int(byte, 2)
    ascii_text += chr(decimal)

print(ascii_text)
