'''
    @Author: Y.Mani Theja
    @Date: 17-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to conert number to its 8-bit binary representation.

'''
def to_binary(n):
    """
    Converts a number to its 8-bit binary representation.
    """
    return bin(n)[2:].zfill(8)

def swap_nibbles(n):
    """
    Swaps the nibbles of an 8-bit binary number.
    """
    binary_str = to_binary(n)
    swapped_binary_str = binary_str[4:] + binary_str[:4]
    return int(swapped_binary_str, 2)

def is_power_of_two(n):
    """
    Checks if a number is a power of 2.
    """
    return n > 0 and (n & (n - 1)) == 0

def main():
    number = int(input("Enter a nonnegative integer: "))
    
    # Convert number to binary and print
    binary_representation = to_binary(number)
    print(f"Binary representation of {number}: {binary_representation}")
    
    # Swap nibbles and print the result
    swapped_number = swap_nibbles(number)
    print(f"After swapping nibbles: {swapped_number}")
    
    # Check if the swapped number is a power of 2 and print the result
    if is_power_of_two(swapped_number):
        print(f"{swapped_number} is a power of 2.")
    else:
        print(f"{swapped_number} is not a power of 2.")

if __name__ == "__main__":
    main()
