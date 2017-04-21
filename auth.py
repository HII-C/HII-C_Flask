
def auth(func):
    def wrapper():
        func()

    return wrapper
