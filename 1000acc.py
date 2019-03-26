from account import Account
from account import db
from random import randint
from faker import Faker
import random
from account import Account, db


def generate_account_number():
	fake_account_number = random.randint(100000,999999)
	while Account.query.filter_by(account_number=fake_account_number).first() != None:
		fake_account_number = random.randint(100000,999999)
	
	return fake_account_number



def generate_pin_number():
	return random.randint(100,999)


def generate_balance():
	return random.randint(0,10000)


def generate_fake_account():
	account = Account (
		account_number = generate_account_number(),
		pin=generate_pin_number(),
		balance=generate_balance()
	)


def generate_accounts(max_number):
	for x in range (max_number):
		account = generate_fake_account()
		db.session.add(account)

	db.session.commit()



def add_cc_name():
	fake = Faker()
	for account in Account.query.all():
		account.name = fake.name()
		account.cc = fake.credit_card_number()
		account.ccexp = fake.credit_card_expire(start='now', end='+10y',date_format="%m/%y")
		account.cvv = fake.credit_card_security_code()
	db.session.commit()

