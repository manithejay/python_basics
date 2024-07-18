'''
    @Author: Y.Mani Theja
    @Date: 17-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to finds the minimum number of notes required to make the change

'''

def calculate_min_notes(change_amount):
    
    """

    description:
        finds the min_notes and combination of note list
    
    parameters:
        change_amount (integer) : the amount that should need to calculate no.of notes and combinations
    
    return:
        min_notes and change_combination

    """

    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    min_notes = 0
    note_combination = []

    for note in notes:
        if change_amount >= note:
            count = change_amount // note
            min_notes += count
            note_combination.extend([note] * count)
            change_amount %= note

    return min_notes, note_combination

def main():
    
    min_notes, change_combination = calculate_min_notes(int(input("enter a change: ")))
    print(min_notes)
    print(change_combination)

if __name__ == "__main__":
    main()