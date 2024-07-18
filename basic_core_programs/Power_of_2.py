'''
@Author: Y.Mani Theja
@Date: 15-07-2024
@Last Modified by: Y.Mani Theja
@Last Modified time: 15-07-2024
@Title : Python program to print powers of 2 that are less than or equal to 2^N

'''

def print_powers_of_2(n):
    
    """
    Description:
        Prints a table of powers of 2 up to 2^N.
    
    Parameters:
        n (int): The maximum exponent for powers of 2.
    
    Returns:
        None: This function prints the powers of 2.
    """
    for i in range(n + 1):
        power_of_2 = 2 ** i
        print(f"2^{i} = {power_of_2}")


def main():
    n = int(input("Enter the power value N: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print_powers_of_2(n)


if __name__ == "__main__":
    main()

