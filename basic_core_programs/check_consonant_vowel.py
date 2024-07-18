'''
@Author: Y.Mani Theja
@Date: 16-07-2024
@Last Modified by: Y.Mani Theja
@Last Modified time: 16-07-2024
@Title : Python program to check if a letter is a vowel or consonant
'''

def check_consonant_vowel(letter):
    """
    Description:
        Checks if a given letter is a vowel or consonant.
    
    Parameters:
        letter (str): The letter to be checked.
    
    Returns:
        None (prints whether the letter is a vowel or consonant)
    """
    if letter.isalpha():
        if letter.upper() in 'AEIOU':
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")
    else:
        print(f"{letter} is not a valid alphabet")

def main():
    letter = input("Enter a letter: ")
    check_consonant_vowel(letter)

if __name__ == "__main__":
    main()
