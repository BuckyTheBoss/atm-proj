from flask import Flask, render_template, request, redirect, url_for, session
from account import Account
from account import app, db

app.secret_key = b'J.;0ajk>,m8jkLIn89hans*jkj90($'

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		account_number = request.form['account-number']
		pin = request.form['pin']
		account = Account.query.filter_by(account_number=account_number).first()
		if account != None:
			if account.pin == int(pin):
				session['account_number'] = account_number
				return redirect(url_for('menu'))

	return render_template('index.html')



@app.route('/menu/')
def menu():
	account_number = session['account_number']
	account = Account.query.filter_by(account_number=account_number).one()
	return render_template('menu.html', account=account)



@app.route('/withdrawal', methods=['POST', 'GET'])
def withdrawal():
  account_number = session['account_number']
  account = Account.query.filter_by(account_number=account_number).one()
  if request.method == 'POST':
    amount = request.form['amount']
    account.balance = account.balance - int(amount)
    db.session.commit()

    return redirect( url_for('menu') )

  return render_template('withdrawal.html')



@app.route('/deposit', methods=['POST', 'GET'])
def deposit():
  account_number = session['account_number']
  account = Account.query.filter_by(account_number=account_number).one()
  if request.method == 'POST':
    amount = request.form['amount']
    account.balance = account.balance + int(amount)
    db.session.commit()
    return redirect( url_for('menu') )

  return render_template('deposit.html')