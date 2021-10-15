import time

def calculate_time(func):
    '''This is a decorator that counts how long the function takes'''
    def wrapper():
        '''created a wrapper function to take existing functions and 'wrap' them without changing them'''
        initial = time.time()
        #takes the initial time
        call_func = func()
        #calls the function being timed
        end = time.time()
        #takes the time after running the function
        totaltime = end - initial
        # by getting the time from the beginning and the end you get the total run time
        print("Total time: " + str(totaltime))
        #prints the total runtime
        return call_func
    return wrapper

@calculate_time 
def function_used():
    """this is a test function that uses time.sleep to delay the time by 2 seconds."""
    time.sleep(2)
    #delays the timer by 2 seconds.
    return

calculate_time(function_used())
