# python decorator function
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()  # call the actual function that was passed in
    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


@delay_decorator
def say_bye():
    print("bye")


def say_greeting():
    print("see you later?")


# decorated function calls
say_hello()
say_bye()

# another way to do decorated function calls
decorated_function = delay_decorator(say_greeting)
decorated_function()


