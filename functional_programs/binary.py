'''
    @Author: Y.Mani Theja
    @Date: 17-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to Convert a decimal number to its binary representation

'''
def to_binary(n):
    """
    Convert a decimal number to its binary representation.

    Parameters:
        n (int): Decimal number to convert to binary

    Returns:
        str: Binary representation of the decimal number
    """
    if n < 0:
        raise ValueError("Only nonnegative integers can be converted to binary")

    # Edge case for 0
    if n == 0:
        return '0'

    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    # Ensure padding to represent 4 bytes (32 bits)
    padded_binary = binary.zfill(4)

    return padded_binary

# Test the to_binary function
if __name__ == "__main__":
    try:
        n = int(input("Enter a nonnegative integer to convert to binary: "))
        binary_representation = to_binary(n)
        print(f"The binary representation of {n} is: {binary_representation}")
    except ValueError as ve:
        print(f"Error: {ve}")
