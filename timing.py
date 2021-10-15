import time

def calculate_time(func):
    '''This is a decorator that counts how long the function takes'''
    def wrapper():
        '''created a wrapper function to take existing functions and 'wrap' them without changing them'''
        initial = time.time()
        #gets the initial time
        func()
        #runs the function
        totaltime = time.time() - initial
        #gets the current time and subtracts it with initial time to get total time
        print("Total time: " + str(totaltime))
    return wrapper

@calculate_time 
def function_used():
    """this is a test function that uses time.sleep to delay the time by 2 seconds."""
    time.sleep(2)
    #delays the timer by 2 seconds.
    return

calculate_time(function_used())
