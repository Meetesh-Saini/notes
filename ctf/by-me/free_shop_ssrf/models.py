from api import db

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_code = db.Column(db.String(30), nullable=False)
    discount = db.Column(db.Integer, nullable=False)