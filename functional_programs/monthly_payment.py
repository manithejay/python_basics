'''
    @Author: Y.Mani Theja
    @Date: 17-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Calculate the monthly payment for a loan.

'''

def monthly_payment(P, Y, R):

    """

    description:
        to calculate monthly payment
    
    Parameters:
        P(integer) - Principle , Y(integer) - year, R(integer) - rate of intrest
    
    Returns:
        monthly payment

    """
    
    r = R / 12 * 100
    n = Y * 12 
    monthly_payment = P * r / ( 1 - (1+r) ** (-n) )
    return monthly_payment

def main():

    P = int(input())
    Y = int(input())
    R = int(input())
    monthlypayment = monthly_payment(P, Y, R)
    print(monthlypayment)


if __name__ == "__main__":
    main()