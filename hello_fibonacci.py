import os
from flask import Flask, request

app = Flask(__name__)

# Function for nth Fibonacci number
def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


@app.route("/")
def hello():
    num_param = request.args.get("num", "1")  # Get the 'num' parameter from the URL query string
    num = int(num_param)

    fib_result = Fibonacci(num)
    return f"Hello fibonacci!\nI'm trying to make it work. RELAX and try again!!\nApp: Fibonacci({num}) = {fib_result}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
