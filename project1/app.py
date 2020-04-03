from flask import Flask, render_template, jsonify, request
from classes import *
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://dctrbzumwxwvxy:d9f3c10d641a04f27617fc2b950f0319119e8c461e4eaadca60d4567be4b6a00@ec2-54-210-128-153.compute-1.amazonaws.com:5432/d5tda9sutqok51"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/registration")
def registration():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)

@app.route("/course_creation")
def course_creation():
    return render_template("courseadd.html")

@app.route("/register", methods=["POST"])
def register():
    # Get form information.
    name = request.form.get("name")
    password = request.form.get("password")
    username = request.form.get("username")
    course_id=request.form.get("course_id")
    course_password=request.form.get("coursepassword")

    course = Course.query.filter(Course.id == course_id).filter(
                                Course.password == course_password).first()
    if not course:
        return render_template("error.html", message="Course name or password are wrong.")
    
    # Add student
    course.add_student(name,username,password)
    return render_template("success.html")

@app.route("/create_course", methods=["POST"])
def create_course():
    course_name=request.form.get("coursename")
    course_password=request.form.get("coursepassword")
    c=Course(name=course_name,password=course_password)
    db.session.add(c)
    db.session.commit()
    return render_template("success.html")

@app.route("/models")
def models():
    return render_template('models.html')

@app.route("/runmodel", methods=["POST"])
def runmodel():
    word=request.form.get("word")
    model=json.loads(request.form.get('model'))
    dfa = Dfa(model)
    if(dfa.run(word)):
        return jsonify({'answer':True})
    return jsonify({'answer':False})








        
