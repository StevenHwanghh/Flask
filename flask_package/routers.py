from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from flask_package import app, db, bcrypt
from flask_package.forms import RegistrationForm, LoginForm
from flask_package.models import User
from flask_login import login_user, logout_user, current_user

feedback_list = []


def addtofeedbacklist(feedback):
    feedback_list.append(dict(
        feedback=feedback,
        username='Steven',
        recordtime=datetime.utcnow()
    ))

def new_feedback(num):
    return sorted(feedback_list, key=lambda item: item['recordtime'], reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", latest_feedback=new_feedback(3))


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedbackmsg = request.form['feedback']
        addtofeedbacklist(feedbackmsg)
        app.logger.debug('Stored feedback; ' + feedbackmsg)
        flash("Your Feedback: " + feedbackmsg + " is submitted! Thank you!")
        return redirect(url_for('index'))

    return render_template("feedback.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash("Account created !")
            return redirect(url_for('login'))
        if form.errors:
            flash("Validation Errors:" + str(form.errors))
            app.logger.error('ValidationError:\n' + str(form.errors))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Authentication failed !")
                app.logger.error('"Authentication failed !"')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
