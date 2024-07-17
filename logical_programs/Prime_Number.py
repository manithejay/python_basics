'''
    @Author: Y.Mani Theja
    @Date: 12-07-2024
    @Last Modified by: Y.Mani Theja
    @Last Modified time: 12-07-2024
    @Title : Python program to check if a given number is a prime number

'''

def is_prime_number(number):

    """
    Description:
        Checks whether a given number is a prime number or not.
    
    Parameters:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is a prime number, False otherwise.
    """

    if number <= 1:
        return False
    
    for i in range(2,number//2+1):
        if number % i == 0:
            return False
    return True


def main():
    
    test_number = int(input("Enter the number: "))
    if is_prime_number(test_number):
        print(f"{test_number} is a prime number.")
    else:
        print(f"{test_number} is not a prime number.")


if __name__ == "__main__":
    main()

