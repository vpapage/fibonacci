import os
from flask import Flask
app = Flask(__name__)

NUM = os.environ.get('NUM', '10')


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
        return Fibonacci(n-1) + Fibonacci(n-2)

@app.route("/")
def hello():
    print(f"Fibonacci({NUM})", Fibonacci(NUM))
    return f"Hello Vasiliki!\nI'm trying to make it work RELAX and try again !!\nApp: Fibonacci({NUM})"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
