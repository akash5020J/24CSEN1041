def convert_number(num):
    print(f"Decimal: {num}")
    print(f"Binary: {bin(num)}")
    print(f"Octal: {oct(num)}")
    print(f"Hexadecimal: {hex(num)}")

# Driver code
if __name__ == "__main__":
    number = int(input("Enter a decimal number: "))
    convert_number(number)

OUTPUT:
Enter a decimal number: 25
Decimal: 25
Binary: 0b11001
Octal: 0o31
Hexadecimal: 0x19
