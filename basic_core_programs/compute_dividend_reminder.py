'''
    @Author: Y.Mani Theja
    @Date: 15-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to compute the quotient and remainder

'''

def compute_quotient_remainder(dividend, divisor):
    
    """
    Description:
        This function computes the quotient and remainder of a given dividend and divisor.
    
    Parameters:
        dividend (int): The number to be divided.
        divisor (int): The number by which to divide.
    
    Returns:
        None: This function prints the quotient and remainder.
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    print("Quotient:", quotient)
    print("Remainder:", remainder)

def main():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    compute_quotient_remainder(dividend, divisor)

if __name__ == "__main__":
    main()
