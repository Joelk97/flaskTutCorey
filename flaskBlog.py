from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e41e7070b8e306efd1bbab0a552633d7' # got via Pathon >>> import secrets >>> secrets.token_hex(16)

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
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=post, title="Home - Blog")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)