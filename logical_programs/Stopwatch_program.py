'''
    @Author: Y.Mani Theja
    @Date: 13-07-2024
    @Last Modified by: Y.Mani Theja
    @Last Modified time: 17-07-2024
    @Title : Python program to calculate the time from start time to end time for elapsed time

'''

import time

def end_time():
    
    """

    description:
        This function is get the end time.
    
    parameters:
        it takes none parameters
        
    return:
        it returns none    

    """

    input("press enter to stop the stop watch: ")
    print("time ended: ")
    global end_time
    end_time=time.time()
    print(end_time)

def start_time():
    
    """
    description:
        This function is get the starting time.
    
    parameters:
        it takes none parameters
        
    return:
        it returns none     

    """

    input("press enter to start the stop watch: ")
    print("time started: ")
    global start_time
    start_time=time.time()
    print(f"{start_time}")
    end_time()
   
start_time()

elapsed_time = end_time - start_time
print(elapsed_time, "is elapsed time")
