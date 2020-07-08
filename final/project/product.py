from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Product
from .models import Category
from .forms import ProductForm
from . import db
import sys
import json
import requests

product = Blueprint('product', __name__)

@product.route('/product')
@login_required
def indexp():
    products = Product.query.all()
    return render_template('product.html',products=products)

@product.route("/insertp", methods=["GET", "POST"])
@login_required
def insertp():
    form = ProductForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    if form.validate_on_submit():
        p = Product()
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("product.indexp"))
    return render_template("insert_product.html", form=form)

@product.route("/jsonp", methods=["GET", "POST"])
@login_required
def exportp():
    products = [{'codigo': c.id, 'name':c.name, 'quantity': c.quantity, 'category': c.category.name} for c in Product.query]
    
    return json.dumps({'products':products})

@product.route("/editp/<int:id>", methods=["GET", "POST"])
def atualizarp(id):
    form = ProductForm()
    product = Product.query.filter_by(id=id).first()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        return redirect(url_for("product.indexp"))

    form.insert_data(product)
    return render_template("edit_product.html", form=form)


@product.route("/deletep/<int:id>")
def excluirp(id):
    product = Product.query.filter_by(id=id).first()

    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("product.indexp"))