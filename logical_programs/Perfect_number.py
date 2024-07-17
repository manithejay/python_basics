'''
    @Author: Y.Mani Theja
    @Date: 12-07-2024
    @Last Modified by: Y.Mani Theja
    @Last Modified time: 12-07-2024
    @Title : Python program to check if a given number is a perfect number

'''

def is_perfect_number(number):

    """
    Description:
        Checks whether a given number is a perfect number or not.
        A perfect number is a positive integer that is equal to the sum of its proper divisors,
        excluding itself.
    
    Parameters:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect number, False otherwise.
    """

    if number < 1:
        return False
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number


def main():
    
    test_number = int(input("Enter the number: "))
    if is_perfect_number(test_number):
        print(f"{test_number} is a perfect number.")
    else:
        print(f"{test_number} is not a perfect number.")


if __name__ == "__main__":
    main()

