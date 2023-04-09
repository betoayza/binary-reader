from termcolor import colored

""" 
    TRANSLATOR BINARY <-> TEXT
"""

print("\nWellcome to Binary Translator 2023!")

is_running_main = True
while is_running_main:
    try:
        option = int(input(
            "\nWhat you wanna do?:\n   1. Binary -> Text\n   2. Text -> Binary\n   3. Exit\n   Choice: "))

        if option == 1:
            is_running_1 = True
            while is_running_1:
                try:
                    binary_code = input("\nEnter binary code: ")
                    if not binary_code.isspace() and binary_code:
                        bytes_list = binary_code.split()

                        ascii_text = ""
                        for byte in bytes_list:
                            decimal = int(byte, 2)
                            ascii_text += chr(decimal)

                        print("Result is: ", colored(ascii_text, 'cyan'))
                        is_running_1 = False
                    else:
                        print("You must enter something...")
                except:
                    print("That's not valid, ha!...")
        elif option == 2:
            is_running_2 = True
            while is_running_2:
                text = input("\nEnter text: ")
                list_bytes_str = []
                if text:
                    list_chars = list(text)
                    for char in list_chars:
                        # convert each one: char -> decimal -> byte_str
                        list_bytes_str.append(format(ord(char), '08b'))

                    bytes_str = " ".join(list_bytes_str)
                    print("Result is:", colored(bytes_str, 'cyan'))
                    is_running_2 = False
                else:
                    print("You must enter something...")

        else:
            is_running_main = False
    except:
        print("Wrong answer...")
print("\nThanks, see on!")
