from flaskBlog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from flaskBlog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskBlog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



post = [
    { 
        "title": "Titolo bello",
        "content": "First post",
        "author": "corey sdvsd",
        "date_posted": "27.01.2023" 
    },
    {
        "title": "Titolo bello2",
        "content": "First post2",
        "author": "Joel fdn",
        "date_posted": "27.01.2023" 
    }
    ,
    {
        "title": "Titolo bello3",
        "content": "First post2",
        "author": "Joel fdn",
        "date_posted": "30.01.2023" 
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=post, title="Home - Blog")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user, remember=form.remember.data)
           next_page = request.args.get('next')
           if next_page:
               return redirect(next_page)
           else:
               return redirect(url_for('home'))
        else:
            flash('Log In Unsuccessfull, Please check your email and your password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=['GET','POST'])
@login_required     # to navigate to this route you need to be logged in
def account():
    form = UpdateAccountForm()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)