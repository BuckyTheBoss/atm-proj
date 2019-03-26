from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# 
balance = 629
# 


@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    acc_n = request.form['account-number']
    acc_p = request.form['pin']

    if acc_n == '12345' and acc_p == '789':
      return redirect( url_for('menu') )

  return render_template('index.html')


@app.route('/menu')
def menu():
  return render_template('menu.html', balance=balance)


@app.route('/withdrawal', methods=['POST', 'GET'])
def withdrawal():
  if request.method == 'POST':
    amount = request.form['amount']
    # balance = balance - amount
    return redirect( url_for('menu') )

  return render_template('withdrawal.html')


@app.route('/deposit', methods=['POST', 'GET'])
def deposit():
  if request.method == 'POST':
    amount = request.form['amount']
    # balance = balance - amount
    return redirect( url_for('menu') )

  return render_template('deposit.html')