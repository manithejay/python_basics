'''
    @Author: Y.Mani Theja
    @Date: 15-07-2024
    @Last Modified by: Y.Mani Theja
    @Last Modified time: 15-07-2024
    @Title : Python program to check if a year is a Leap Year or not

'''

def leap_year(year):

    """
    Description:
        This function checks whether a given year is a leap year or not.
    
    Parameters:
        year (int): The year to check for being a leap year.
    
    Returns:
        None: This function prints whether the year is a leap year or not.
    """
    if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
        print(f"The entered year {year} is a leap year.")
    else:
        print(f"The entered year {year} is not a leap year.")


def main():
    year = int(input("Enter the year: "))
    leap_year(year)
    

if __name__ == "__main__":
    main()

