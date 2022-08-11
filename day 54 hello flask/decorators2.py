# python decorator function

import time
from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()  # call the actual function that was passed in
    return wrapper_function


@delay_decorator
def say_hello():
    print("delayed hellooooo")


@app.route('/')
def main_hello():
    return "home page hello!!"


@delay_decorator
def say_bye():
    print("bye")


def say_greeting():
    print("see you later?")


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye! defined decorators"


# decorated function calls
say_hello()
say_bye()

# another way to do decorated function calls
decorated_function = delay_decorator(say_greeting)
decorated_function()


if __name__ == "__main__":    # app is run within hello.py
    app.run(debug=True)   # run flask within this code instead of 'flask run'
