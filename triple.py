def tripler(func):
    """this decorator will call the function three times"""
    def wrapper(*arg,**kwargs):
        func()
        func()
        func()
        #calls the function three times
    return wrapper

@tripler
def test():
    """this is a test function that will print hello"""
    print("hello")

tripler(test)
