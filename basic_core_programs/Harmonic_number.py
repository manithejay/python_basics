'''
    @Author: Y.Mani Theja
    @Date: 15-07-2024
    @Last Modified by: Y.Mani Theja
    @Last Modified time: 15-07-2024
    @Title : Python program to calculate the nth Harmonic Number

'''

def nth_harmonic_number(number):

    """
    Description:
        Calculates the nth Harmonic Number.
    
    Parameters:
        number (int): The nth value to calculate the Harmonic Number.
    
    Returns:
        float: The nth Harmonic Number.
    """
    harmonic = 0
    for i in range(1, number + 1):
        harmonic += 1 / i
    return harmonic

def main():

    number = int(input("Enter the Harmonic Value N (N should be non-zero): "))
    if number <= 0:
        print("Please enter a non-zero positive integer.")
    else:
        result = nth_harmonic_number(number)
        print(f"The {number}th Harmonic Value is: {result:.4f}")
        

if __name__ == "__main__":
    main()
