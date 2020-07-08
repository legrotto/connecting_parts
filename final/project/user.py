from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User
from .forms import UserForm
from . import db

user = Blueprint('user', __name__)

@user.route('/user')
@login_required
def indexu():
    users = User.query.all()
    return render_template('user.html',users=users)

@user.route("/editu/<int:id>", methods=["GET", "POST"])
def editu(id):
    form = UserForm()
    user = User.query.filter_by(id=id).first()

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("user.indexu"))

    form.insert_data(user)
    return render_template("edit_user.html", form=form)

@user.route("/deleteu/<int:id>")
def excluir(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    
    return redirect(url_for("user.indexu"))
