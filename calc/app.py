# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

MATH = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}

@app.route('/math/<operation>')
def calculator(operation):
    """ calculates specified information with two integers """ 
    
    operation = MATH[operation]
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = operation(a, b)

    return f"<h1>TOTAL: {total}</h1>"

