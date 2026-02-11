from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required
)
from config import Config
from models import db, User, Student
from werkzeug.utils import secure_filename
import os

# --------------------------------
# APP SETUP
# --------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# Upload configuration
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database
db.init_app(app)

# Login manager
login_manager = LoginManager(app)
login_manager.login_view = "login"

# --------------------------------
# LOGIN MANAGER
# --------------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --------------------------------
# INITIAL DB + ADMIN
# --------------------------------
with app.app_context():
    db.create_all()
    if not User.query.first():
        admin = User(username="admin", password="admin123")
        db.session.add(admin)
        db.session.commit()

# --------------------------------
# LOGIN
# --------------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and user.password == request.form["password"]:
            login_user(user)
            return redirect(url_for("dashboard"))
        flash("Invalid username or password")
    return render_template("login.html")

# --------------------------------
# DASHBOARD
# --------------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    students = Student.query.all()

    total_students = Student.query.count()
    active_students = Student.query.filter_by(status="Active").count()
    graduated_students = Student.query.filter_by(status="Graduated").count()
    dropped_students = Student.query.filter_by(status="Dropped").count()

    return render_template(
        "dashboard.html",
        students=students,
        total_students=total_students,
        active_students=active_students,
        graduated_students=graduated_students,
        dropped_students=dropped_students
    )

# --------------------------------
# ADD STUDENT
# --------------------------------
@app.route("/add", methods=["GET", "POST"])
@login_required
def add_student():
    if request.method == "POST":

        photo_file = request.files.get("photo")
        doc_file = request.files.get("document")

        photo_path = None
        doc_path = None

        if photo_file and photo_file.filename:
            photo_name = secure_filename(photo_file.filename)
            photo_path = f"uploads/{photo_name}"
            photo_file.save(os.path.join("static", photo_path))

        if doc_file and doc_file.filename:
            doc_name = secure_filename(doc_file.filename)
            doc_path = f"uploads/{doc_name}"
            doc_file.save(os.path.join("static", doc_path))

        student = Student(
            roll_no=request.form["roll"],
            name=request.form["name"],
            department=request.form["department"],
            course=request.form["course"],
            year=int(request.form["year"]),   # ✅ FIXED
            email=request.form["email"],
            phone=request.form["phone"],
            status=request.form["status"],    # Active / Graduated / Dropped
            photo=photo_path,
            document=doc_path
        )

        db.session.add(student)
        db.session.commit()

        flash("Student added successfully")
        return redirect(url_for("dashboard"))

    return render_template("add_student.html")

# --------------------------------
# EDIT STUDENT
# --------------------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == "POST":
        student.roll_no = request.form["roll"]
        student.name = request.form["name"]
        student.department = request.form["department"]
        student.course = request.form["course"]
        student.year = int(request.form["year"])  # ✅ FIXED
        student.email = request.form["email"]
        student.phone = request.form["phone"]
        student.status = request.form["status"]

        photo_file = request.files.get("photo")
        doc_file = request.files.get("document")

        if photo_file and photo_file.filename:
            photo_name = secure_filename(photo_file.filename)
            student.photo = f"uploads/{photo_name}"
            photo_file.save(os.path.join("static", student.photo))

        if doc_file and doc_file.filename:
            doc_name = secure_filename(doc_file.filename)
            student.document = f"uploads/{doc_name}"
            doc_file.save(os.path.join("static", student.document))

        db.session.commit()
        flash("Student updated successfully")
        return redirect(url_for("dashboard"))

    return render_template("edit_student.html", student=student)

# --------------------------------
# DELETE STUDENT
# --------------------------------
@app.route("/delete/<int:id>")
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash("Student deleted")
    return redirect(url_for("dashboard"))

# --------------------------------
# LOGOUT
# --------------------------------
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# --------------------------------
# RUN
# --------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)





    
