'''
    @Author: Y.Mani Theja
    @Date: 15-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to swap two numbers

'''

def swap(num1, num2):

    """
    Description:
        The function takes two arguments and swaps their values.
    
    Parameters:
        num1 (int): The first number.
        num2 (int): The second number.
    
    Returns:
        None: This function prints the swapped values.
    """
    num1, num2 = num2, num1
    print("After swapping:")
    print("First number:", num1)
    print("Second number:", num2)
    

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Before swapping:")
    print("First number:", num1)
    print("Second number:", num2)
    swap(num1, num2)


if __name__ == "__main__":
    main()
