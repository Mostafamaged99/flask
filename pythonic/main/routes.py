from flask import Blueprint
from pythonic.models import  Lesson, Course
from flask import render_template

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    lessons = Lesson.query.order_by(Lesson.date_posted.desc()).paginate(page=1, per_page=6) 
    courses = Course.query.paginate(page=1, per_page=3)
    return render_template("home.html", lessons=lessons, courses=courses)


@main.route("/about")
def about():
    return render_template("about.html", title="About")