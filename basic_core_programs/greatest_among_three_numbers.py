'''
    @Author: Y.Mani Theja
    @Date: 16-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to find the greatest of three numbers

'''

def greatest_number(number1, number2, number3):

    """
    Description:
        Function to find the greatest number among three given numbers.
    
    Parameters:
        number1 (int): The first number.
        number2 (int): The second number.
        number3 (int): The third number.
        
    Returns:
        int: The greatest number among the three.
    """
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number3:
        return number2
    else:
        return number3

def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    greatest = greatest_number(number1, number2, number3)
    print(f"The greatest number is {greatest}")


if __name__ == "__main__":
    
    main()



