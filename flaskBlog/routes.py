from flaskBlog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from flaskBlog.forms import RegistrationForm, LoginForm
from flaskBlog.models import User, Post



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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log In Unsuccessfull, Please check your email and your password', 'danger')
    return render_template("login.html", title='Login', form=form)

