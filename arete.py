# from flask import Flask, render_template, url_for, flash,redirect
# from forms import RegistrationForm, LoginForm
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "fb30ae82cc1c973f34ab75697e68759077c4dbf0705c67c7"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///arete.db"
# #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# db = SQLAlchemy(app)

# lessons = [
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
# ]

# courses = [
#     {
#         "name": "Python",
#         "icon": "python.svg",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Data Analysis",
#         "icon": "analysis.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Machine Learning",
#         "icon": "machine-learning.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Web Design",
#         "icon": "web.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Blockchain",
#         "icon": "blockchain.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Tips & Tricks",
#         "icon": "idea.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
# ]


# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home.html", lessons=lessons, courses=courses)


# @app.route("/about")
# def about():
#     return render_template("about.html", title="About")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f"Registration Successful for {form.username.data}","success")
#         return redirect(url_for("home"))
#     return render_template("register.html",title="Register",form=form)

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == "maged@gmail.com" and form.password.data == "asd123456":
#             flash(f"Login Successful for {form.email.data}","success")
#             return redirect(url_for("home"))
#         else:
#             flash("Login Unsuccessful. Please check username and password","danger")
#     return render_template("login.html",title="Login",form=form)

# if __name__ == "__main__":
#     app.run(debug=True)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fname = db.Column(db.String(25), unique=False, nullable=False)
#     lname = db.Column(db.String(25), unique=False, nullable=False)
#     username = db.Column(db.String(25), unique=True, nullable=False)
#     email = db.Column(db.String(125), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default="default.png")
#     password = db.Column(db.String(60), nullable=False)
#     lessons = db.relationship("Lesson", backref="author", lazy=True)
#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.username}', '{self.email}', '{self.image_file}')"

# class Lesson(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     # course = db.Column(db.String(100), nullable=False)
#     # author = db.Column(db.String(100), nullable=False)
#     thumbnail = db.Column(db.String(100), nullable=False,default= "thumbnail.jpg")
#     slug = db.Column(db.String(100), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
#     course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
#     def __repr__(self):
#         return f"Lesson('{self.title}', '{self.date_posted}')"

# class Course(db.Model): 
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False,unique=True)
#     icon = db.Column(db.String(100), nullable=False,default= "default.png")
#     description = db.Column(db.String(150), nullable=False)
#     lessons = db.relationship("Lesson", backref="course_name", lazy=True)
#     def __repr__(self):
#         return f"Course('{self.title}')"

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from arete import app, db

with app.app_context():
    db.create_all()

app = Flask(__name__)
app.config["SECRET_KEY"] = "fb30ae82cc1c973f34ab75697e68759077c4dbf0705c67c7"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///arete.db"
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), unique=False, nullable=False)
    lname = db.Column(db.String(25), unique=False, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.png")
    password = db.Column(db.String(60), nullable=False)
    lessons = db.relationship("Lesson", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.username}', '{self.email}', '{self.image_file}')"

# Define the Lesson model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(db.String(100), nullable=False, default="thumbnail.jpg")
    slug = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    def __repr__(self):
        return f"Lesson('{self.title}', '{self.date_posted}')"

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    icon = db.Column(db.String(100), nullable=False, default="default.png")
    description = db.Column(db.String(150), nullable=False)
    lessons = db.relationship("Lesson", backref="course_name", lazy=True)

    def __repr__(self):
        return f"Course('{self.title}')"

lessons = [
    # your lesson dictionary here...
]

courses = [
    # your course dictionary here...
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", lessons=lessons, courses=courses)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Registration Successful for {form.username.data}", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "maged@gmail.com" and form.password.data == "asd123456":
            flash(f"Login Successful for {form.email.data}", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    # Initialize the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)
