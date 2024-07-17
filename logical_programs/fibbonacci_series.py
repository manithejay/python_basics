'''
    @Author: Y.Mani Theja
    @Date: 12-07-2024
    @Last Modified by: Y.Mani Theja
    @Last Modified time: 12-07-2024
    @Title : Python program to generate the Fibonacci series

'''

def fibonacci_series(first_number, second_number, nth_number):

    """
    Description:
        Generates the Fibonacci series up to the nth number.
    
    Parameters:
        first_number (int): The first number of the Fibonacci series.
        second_number (int): The second number of the Fibonacci series.
        nth_number (int): The number up to which Fibonacci series is generated.
    
    Returns:
        None (prints the Fibonacci series)
    """
    if nth_number == 1:
        print(first_number)
    elif nth_number == 2:
        print(first_number, second_number)
    else:
        print(first_number, second_number, end=" ")
        for i in range(nth_number - 2):
            third_number = first_number + second_number
            print(third_number, end=" ")
            first_number = second_number
            second_number = third_number

def main():
    nth_number = int(input("Enter the number up to which Fibonacci series should be generated: "))
    first_number = int(input("Enter the first number of the series: "))
    second_number = int(input("Enter the second number of the series: "))
    
    fibonacci_series(first_number, second_number, nth_number)

if __name__ == "__main__":

    main()

