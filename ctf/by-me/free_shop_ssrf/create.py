import csv
from api import db, api
from models import *

FLAG = "ctf{hey_th!s_might_be_flag}"

def write_flag():
    with open("flag.txt", "w") as f:
        f.write(FLAG)


def load(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)

def update_product():
    reader = load("product.csv")
    with api.app_context():
        db.session.query(Price).delete()
        for row in reader:
            new_row = Price(product=row[0], price=row[1])
            db.session.add(new_row)
            db.session.commit()

def update_sale():
    reader = load("sale.csv")
    with api.app_context():
        db.session.query(Sale).delete()
        for row in reader:
            new_row = Sale(sale_code=row[0], discount=row[1])
            db.session.add(new_row)
            db.session.commit()

write_flag()
update_product()
update_sale()