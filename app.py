from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius>')
def f(celsius=""):
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    return "{} Celsius is {:.2f} Fahrenheit".format(celsius, fahrenheit)


@app.route('/c/<fahrenheit>')
def c(fahrenheit=""):
    celsius = fahrenheit_to_celsius(float(fahrenheit))
    return "{} Fahrenheit is {:.2f} Celsius".format(fahrenheit, celsius)


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
