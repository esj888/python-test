# in powershell administrator:
#    1) PS C:\python-test\day 54 hello flask> python -m flask run
# or 2) PS C:\python-test\day 54 hello flask> flask run
# http://127.0.0.1:5000


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":    # app is run within hello.py
    app.run()   # run flask within this code instead of 'flask run'
