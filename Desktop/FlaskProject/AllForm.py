from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import *
from wtforms.validators import DataRequired

# ====================================
#               Form
# ====================================

class LoginForm(FlaskForm):
    email = StringField("Enter your email:", validators=[DataRequired()])
    password = PasswordField("Entet your password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    search = StringField()
    submit = SubmitField()

class RegisterForm(FlaskForm):
    fname = StringField("Enter Firstname:", validators=[DataRequired()])
    lname = StringField("Enter Lastname:", validators=[DataRequired()])
    email = EmailField("Enter Email:", validators=[DataRequired()])
    password = PasswordField("Enter Password:", validators=[DataRequired()])
    conpassword = PasswordField("Confirm Password:", validators=[DataRequired()])
    accept = BooleanField("I accept term and policy")
    file = FileField("Select Profile Image:", validators=[FileAllowed(['jpg', 'png'], 'Image Only!')])
    submit = SubmitField("Submit")

class DeliveryForm(FlaskForm):
    owner = BooleanField("Shipping to Me")
    fname = StringField("Firstname :")
    lname = StringField("Lastname :")
    email = EmailField("Email :")
    address = StringField("Address :")
    province = SelectField("Province :", choices=[("#","เลือกจังหวัด")])
    district = SelectField("District :", choices=[("#","เลือกอำเภอ")])
    subDistrict = SelectField("Subdistrict :", choices=[("#","เลือกตำบล")])
    postcode = StringField("Postcode :")
    telNumber = StringField("Phone Number :")
    
    other = BooleanField("Shipping to Other")
    fname2 = StringField("Firstname :")
    lname2 = StringField("Lastname :")
    email2 = EmailField("Email :")
    address2 = StringField("Address :")
    province2 = SelectField("Province :", choices=[("#","เลือกจังหวัด")])
    district2 = SelectField("District :", choices=[("#","เลือกอำเภอ")])
    subDistrict2 = SelectField("Subdistrict :", choices=[("#","เลือกตำบล")])
    postcode2 = StringField("Postcode :")
    telNumber2 = StringField("Phone Number :")

    Tax = BooleanField("Require Tax Invoice")
    Tax_company = StringField("Tax Invoice Name:")
    Tax_payer = StringField("Tax Payer Number:")
    Tax_location = StringField("Tax Invoice Address:")

    submit = SubmitField("Submit")

class ProductForm(FlaskForm):
    type = SelectField("Select Type:", choices=[("SR","ข้าวเหนียว"),("WR","ข้าวจ้าว"),("IR","ข้าวนำเข้า"),("HR","ข้าวเพื่อสุขภาพ")])
    group = SelectField("Select Group:", choices=[("PM","Promotion"),("BS","Boxset"),("NM","Normal"),("PO","Pre-Order")])
    code = StringField("Enter Product Code:")
    name = StringField("Enter Product Name:")
    price = StringField("Enter Product Price:")
    deal = StringField("Enter Product Deal:")
    file = FileField("Select Product Image:", validators=[ FileAllowed(['jpg', 'png'], 'Image Only!')])
    submit = SubmitField("Submit")

class UserPayment(FlaskForm):
    select_choices = BooleanField()
    name = StringField("Please enter your name :")
    email = StringField("Please enter your email :")
    phone = StringField("Please enter your phone number:")
    file = FileField("Select Product Image:", validators=[ FileAllowed(['jpg', 'png'], 'Image Only!')])
    cost = StringField("Amount:")
    date = DateField("Select Date:", format="%Y-%m-%d")
    time = TimeField("Enter Time:", format="%H:%M")
    serial = StringField("Enter Serial Code:")
    description = TextAreaField("Description:")
    submit = SubmitField("Submit")

# class simpleForm(FlaskForm):
#     name = StringField("Enter your name:", validators=[DataRequired()])
#     age = IntegerField("Entet your age")
#     gender = RadioField("What is your gender?", choices=[("M", "male"),("F", "female"),("O","Other")])
#     activity = SelectField("What is your hobbies", choices=[("M", "Music"),("R", "Reading"),("G","Gaming")])
#     color = StringField("What is your flavorite color?")
#     submit = SubmitField("Submit")