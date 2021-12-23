from flask import render_template, url_for, flash, redirect, request
from kaora.forms import RegistrationForm, LoginForm, AddProduct
from kaora import app, bcrypt
from kaora import db
from kaora.models import User, Product, Post
import flask_login
from flask_login import login_user, current_user, logout_user
import os


@app.route("/")
def index():
    return render_template("index.html", title="Homepage", is_active=False)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/travel_blog")
def travel_blog():
    return render_template("travel_blog.html", title="Travel Blog", is_active=True)


@app.route("/gallery")
def gallery():
    return render_template("gallery_by_collections.html", title="gallery")


@app.route("/all_products")
def products():
    return render_template("gallery_all.html", title="gallery")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template("index.html", title="Homepage", is_active=True)
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User.query.filter_by(phone_number=form.phone_number.data).first()
        if new_user is None:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            new_user = User(username=form.username.data,
                            password=hashed_password,
                            email=form.email.data,
                            phone_number=form.phone_number.data,
                            address=form.address.data)
            db.session.add(new_user)
            db.session.commit()
            flash(f"Nice to meet you {form.username.data}! Please login", 'info')
            return redirect(url_for('login'))
        if new_user:
            flash(f"Your'e already a friend. Please login!", 'warning')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_active:
        return render_template("index.html", title="Homepage", is_active=True)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash(f"Please sign up first!", 'danger')
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data) \
                    and user.email == "admin@kaora.com":
                login_user(user, remember=form.remember.data)
                return redirect(url_for('upload_products', is_active=True))
            if not bcrypt.check_password_hash(user.password, form.password.data):
                flash(f"Your password seems to be wrong..", 'danger')
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return render_template("index.html", title="Homepage", is_active=True)
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html", title="Homepage", is_active=False)


@app.route('/upload_products', methods=["GET", "POST"])
def upload_products(is_active=True):
    form = AddProduct()
    if request.method == "POST":
        if request.files:
            product_img = request.files["img"]
            if product_img.filename == '':
                flash('This image must has a name', 'danger')
                return redirect(request.url)
            else:
                product_img.save(os.path.join(app.config['UPLOAD_FOLDER'], product_img.filename))
                new_product = Product(img=product_img.filename,
                                collection=form.collection.data,
                                category=form.category.data,
                                price=form.price.data,
                                is_available=form.is_available.data)

                db.session.add(new_product)
                db.session.commit()
                flash("Image uploaded successfully to the new products' folder!", 'success')
    return render_template('upload_products.html', title='Dashboard', form=form, is_active=is_active)


def allowed_image(filename):
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1]
    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
