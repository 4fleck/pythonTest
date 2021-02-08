from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []
Answer = namedtuple('Answer', ' res num1 num2 sig err')
answers = []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))


@app.route('/calk', methods=['GET'])
def calk():
    return render_template('Calk.html', answers=answers)


@app.route('/result', methods=['POST'])
def result():

    return baseCop(lambda x, y: [(x + y), '+'])


@app.route('/res2', methods=['POST'])
def res2():
    return baseCop(lambda x, y: [(x - y), '-'])


@app.route('/res3', methods=['POST'])
def res3():
    return baseCop(lambda x, y: [(x / y), '/'])


@app.route('/res4', methods=['POST'])
def res4():
    return baseCop(lambda x, y: [(x * y), '*'])

def baseCop(tFunc):
    num1 = request.form['num1']
    num2 = request.form['num2']
    try:

        float(num1)
        float(num2)

    except:
        answers.append(Answer('?', num1, num2, '?', 'ERROR'))
        return redirect(url_for('calk'))

    res = tFunc(float(num1), float(num2))
    answers.append(Answer(res[0], num1, num2, res[1], ' '))

    return redirect(url_for('calk'))


