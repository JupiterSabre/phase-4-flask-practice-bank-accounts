from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# write your models here!

class Bank(db.Model, SerializerMixin):
    __tablename__ = "banks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    accounts = db.relationship("Account", back_populates="bank")
    customers = association_proxy("accounts", "customers")

    serialize_rules = ("-accounts.bank")




class Account(db.Model, SerializerMixin):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, nullable=False)
    account_type = db.Column(db.String, nullable=False)

    bank_id = db.Column(db.Integer, db.ForeignKey("banks.id"))
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.id"))

    bank = db.relationship("Bank", back_populates="accounts")
    customers = db.relationship("Customer", back_populates="accounts")

    serialize_rules = ("-bank.accounts", "customer.accounts")


    @validates("balance")
    def check_balance(self, key, number):
        if number < 0:
            raise ValueError("Balance cannot be negative")
        return number
    



class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    accounts = db.relationship("Account", back_populates="customers")
    banks = association_proxy("accounts", "banks")

    serialize_rules = ("-accounts.customer")


    

