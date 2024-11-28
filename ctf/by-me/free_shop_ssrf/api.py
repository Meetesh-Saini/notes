from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

api = Flask(__name__)
api.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/store.db"
db = SQLAlchemy(api)
admin = Admin(api)

from models import *

with api.app_context():
    db.create_all()

@api.route("/getprice/<pid>")
def get_price(pid):
    product = Price.query.filter(Price.id == pid).first()
    if product is None:
        return Response(status=400)
    return str(product.price)

@api.route("/sale/<sale_code>")
def sale(sale_code):
    coupon = Sale.query.filter(Sale.sale_code == sale_code).first()
    if coupon is None:
        return Response(status=400)
    return str(coupon.discount)

class Price_modelview(ModelView):
    column_list = (
        "id",
        "product",
        "price"
    )
    form_widget_args = {
        "id": {'readonly': True},
        "product": {'readonly': True},
        "price": {'readonly': True},
    }
    form_columns = column_list
    can_create = False
    can_delete = False
    can_edit = False

class Sale_modelview(ModelView):
    column_list = (
        "id",
        "sale_code",
        "discount"
    )
    form_widget_args = {
        "id": {'readonly': True},
        "sale_code": {'readonly': True},
        "discount": {'readonly': True},
    }
    form_columns = column_list
    can_create = False
    can_delete = False
    can_edit = False

admin.add_view(Price_modelview(Price, db.session))
admin.add_view(Sale_modelview(Sale, db.session))
