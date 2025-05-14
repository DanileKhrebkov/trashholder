from flask import Flask
app = Flask(__name__)

def calculate_url(first, second, operation):
    match operation:
        case "-":
            return f"<h3>Result {first-second}</h3>"
        case "+":
            return f"<h3>Result {first+second}</h3>"
        case "*":
            return f"<h3>Result {first*second}</h3>"
        case ":":
            return f"<h3>Result {first/second}</h3>"
        case _:
            return ""
@app.route('/')
def hello():
    return "This is the main page"

@app.route('/<int:first>-<int:second>')
def minus(first,second):
    return calculate_url(first, second, '-')

@app.route('/<int:first>+<int:second>')
def plus(first,second):
    return calculate_url(first, second, '+')

@app.route('/<int:first>*<int:second>')
def mult(first,second):
    return calculate_url(first, second, '*')

@app.route('/<int:first>:<int:second>')
def sub(first,second):
    return calculate_url(first, second, ':')


if __name__ == "__main__":
    app.run(port=8000, debug=True)