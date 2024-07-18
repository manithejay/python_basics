'''
    @Author: Y.Mani Theja
    @Date: 16-07-2024
    @Last Modified by: 
    @Last Modified time: 
    @Title : Python program to simulate flipping a coin and print percentage of Heads and Tails

'''

import random

def flip_coin(num_flips):

    """
    Description:
        Simulates flipping a coin a specified number of times and calculates the percentage of Heads and Tails.
    
    Parameters:
        num_flips (int): The number of times to flip the coin.
    
    Returns:
        float, float: The percentage of Heads and Tails respectively.
    """

    heads = 0
    tails = 0
    
    for flip in range(num_flips):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1
    
    heads_percentage = (heads / num_flips) * 100
    tails_percentage = (tails / num_flips) * 100
    
    return heads_percentage, tails_percentage

def main():
    
    num_flips = int(input("Enter the number of times to flip the coin: "))
    heads_percentage, tails_percentage = flip_coin(num_flips)
    print(f"Percentage of Heads: {heads_percentage:.2f}%")
    print(f"Percentage of Tails: {tails_percentage:.2f}%")


if __name__ == "__main__":
    main()
