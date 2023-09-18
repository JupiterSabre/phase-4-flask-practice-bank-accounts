#!/usr/bin/env python3

from app import app
from models import db, Account, Customer, Bank # models go here
from faker import Faker
import random

faker = Faker()

def create_accounts():
    accounts = []
    balance = [34, 52, 654, 34, 234, 334, 24, 111, 911, 653, 782, 834]
    account_type = ["Checking", "Savings"]
    for _ in range(25):
        account = Account(balance= random.choice(balance),  account_type=random.choice(account_type), bank=random.choice(banks), customers= random.choice(customers))
        accounts.append(account)
    return accounts

def create_banks():
    banks = []
    bank_name = ["Chase", "Washington Mutual", "Bank of America", "Capital One", "Charles Schwab"]
    for _ in range(25):
        bank = Bank(name=random.choice(bank_name))
        banks.append(bank)
    return banks




def create_customers():
    customers = []
    fname = ["Bob", "Kirsten", "Marco", "Enrique", "John", "Parker", "Zulai", "James", "Harold", "Liev", "Josie", "Carol", "Jamie", "Jonathan", "Susan", "Becky", "Rosa", "Rebecca", "Josephine"]
    lname = ["Smith", "Davila", "Einstein", "Lewis", "Chen", "Lee", "Romero", "Pretlow", "Washington", "Davila"]
    for _ in range (25):
        customer = Customer(first_name=random.choice(fname), last_name=random.choice(lname))
        customers.append(customer)
    return customers


if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Account.query.delete()
        Bank.query.delete()
        Customer.query.delete()
        print("Seeding database...")

        customers = create_customers()
        db.session.add_all(customers)
        db.session.commit()

        banks = create_banks()
        db.session.add_all(banks)
        db.session.commit()

        accounts = create_accounts()
        db.session.add_all(accounts)
        db.session.commit()



        print("Seeding complete!")
