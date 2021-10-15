def tripler(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper()

@tripler
def test():
    print("hello")

tripler(test)
