'''
@Author: Y.Mani Theja
@Date: 13-07-2024
@Last Modified by: Y.Mani Theja
@Last Modified time: 13-07-2024
@Title : Python function to reverse a given number
'''

def reverse_number(number):
    """
    Description:
        Reverses a given integer number.
    
    Parameters:
        number (int): The number to be reversed.
    
    Returns:
        int: The reversed number.
    """
    reverse = 0
    
    while number > 0:
        reminder = number % 10
        number = number // 10
        reverse = reverse * 10 + reminder
    
    return reverse

def main():

    number = int(input("Enter a number: "))
    reversed_number = reverse_number(number)
    print(f"The reversed number is: {reversed_number}")
    

if __name__ == "__main__":
    main()

