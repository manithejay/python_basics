'''
    @Author: Y.Mani Theja
    @Date: 17-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to Compute the square root of a nonnegative number using Newton's method.

'''
def sqrt(c):
    """
    Compute the square root of a nonnegative number using Newton's method.

    Parameters:
        c (float): Nonnegative number for which square root is to be computed

    Returns:
        float: Approximate square root of c
    """
    if c < 0:
        raise ValueError("Square root of negative numbers is not defined")

    t = c  # Initial guess for square root
    epsilon = 1e-15  # Desired accuracy

    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2.0

    return t

# Test the sqrt function
if __name__ == "__main__":
    c = float(input("Enter a nonnegative number to find its square root: "))
    
    if c < 0:
        print("Error: Square root of negative numbers is not defined")
    else:
        result = sqrt(c)
        print(f"The square root of {c} is approximately {result:.6f}")
