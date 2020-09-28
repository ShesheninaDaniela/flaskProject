from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/', methods=['POST'])
def result():
    num1 = request.form.get("num1", type=int)
    num2 = request.form.get("num2", type=int)
    operation = request.form.get("operation")
    if (operation == 'Addition'):
        result = num1 + num2
    elif(operation == 'Subtraction'):
        result = num1 - num2
    elif(operation == 'Multiplication'):
        result = num1 * num2
    elif(operation == 'Division'):
        result = num1 / num2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('app.html', entry=entry)


app.run(host='0.0.0.0',port=5000)
