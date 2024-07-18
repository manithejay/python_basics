'''
    @Author: Y.Mani Theja
    @Date: 15-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to check if a number is even or odd

'''

def even_odd(number):

    """
    Description:
        This function checks whether a given number is even or odd.
    
    Parameters:
        number (int): The number to check.
    
    Returns:
        None: This function prints whether the number is even or odd.
    """
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")


def main():
    number = int(input("Enter the number: "))
    even_odd(number)


if __name__ == "__main__":
    main()
