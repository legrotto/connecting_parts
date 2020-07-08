from flask_wtf import FlaskForm 
from wtforms import StringField,IntegerField, PasswordField, BooleanField, SubmitField, HiddenField,SelectField
from wtforms.validators import DataRequired
from .models import Category


class CategoryForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    
    def insert_data(self, category):
        self.name.data = category.name

class ProductForm(FlaskForm):
    name = StringField('Título', validators=[DataRequired()])
    quantity = IntegerField('Quantidade', validators=[DataRequired()])
    category_id = SelectField('Categoria',coerce=int)

    def insert_data(self, product):
        self.name.data = product.name
        self.quantity.data = product.quantity
        self.category_id.data = product.category.id

class UserForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

    def insert_data(self, user):
        self.name.data = user.name
        self.email.data = user.email