'''
    @Author: Y.Mani Theja
    @Date: 15-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to print the prime factors of a number

'''

def prime_factors(N):

    """
    Description:
        The function takes a single integer argument and finds its prime factors.
    
    Parameters:
        N (int): The integer to find the prime factors of.
    
    Returns:
        list: A list of prime factors of the integer N.
    """
    factors = []

    for i in range(2, N // 2 + 1):
        while N % i == 0:
            factors.append(i)
            N //= i
    
    if N > 1:
        factors.append(N)
    return factors

def main():
    N = int(input("Enter a number: "))
    factors_of_number = prime_factors(N)
    print("Prime factors of", N, "are:", factors_of_number)
    

if __name__ == "__main__":
    main()
