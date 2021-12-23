from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, equal_to, Email


class RegistrationForm(FlaskForm):
    username = StringField('Full name:',
                           validators=[DataRequired(), length(min=2, max=20)])
    email = StringField('Email:',
                        validators=[DataRequired(), Email()])
    phone_number = StringField('Phone:',
                               validators=[DataRequired(), length(min=6, max=12)])
    address = StringField('Address:',
                          validators=[DataRequired(), length(max=100)])
    password = PasswordField('Password',
                             validators=[DataRequired(), length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), length(min=2, max=20), equal_to('password')])
    submit = SubmitField('I want to become a friend!')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password',
                            validators=[DataRequired(), length(min=2, max=20)])
    submit = SubmitField('Login')
    remember = BooleanField('Remember Me')


class AddProduct(FlaskForm):
    collection = StringField("Collection:",
                        validators=[DataRequired(), length(min=3)])
    category = StringField("Category:",
                        validators=[DataRequired(), length(min=3)])
    price = StringField("Price:",
                        validators=[DataRequired(), length(min=2)])
    is_available = BooleanField("Is available to sale?",
                                validators=[DataRequired()])
    img = StringField(validators=[DataRequired()])
