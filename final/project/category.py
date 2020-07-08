from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Category, Product
from .forms import CategoryForm
from . import db

category = Blueprint('category', __name__)

@category.route('/category')
@login_required
def index():
    categories = Category.query.all()
    return render_template('category.html',categories=categories)

@category.route("/insert", methods=["GET", "POST"])
@login_required
def insert():
    form = CategoryForm()
    if form.validate_on_submit():
        p = Category()
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("category.index"))
    return render_template("insert_category.html", form=form)

@category.route("/edit/<int:id>", methods=["GET", "POST"])
def atualizar(id):
    form = CategoryForm()
    category = Category.query.filter_by(id=id).first()

    if form.validate_on_submit():
        form.populate_obj(category)
        db.session.commit()
        return redirect(url_for("category.index"))

    form = CategoryForm()
    form.insert_data(category)
    return render_template("edit_category.html", form=form)


@category.route("/delete/<int:id>")
def excluir(id):
    category = Category.query.filter_by(id=id).first()
    db.session.delete(category)
    db.session.commit()
    
    return redirect(url_for("category.index"))