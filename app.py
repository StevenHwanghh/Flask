import os
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from logging import DEBUG
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.secret_key = os.urandom(16)

feedback_list = []

def addtofeedbacklist(feedback):
    feedback_list.append(dict(
        feedback=feedback,
        username='Steven',
        recordtime=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
    ))


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


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
        if form.email.data == "stevenh@ibm.com" and form.password.data == '123':
            redirect(url_for('index'))
        else:
            flash("Authentication failed !")
            app.logger.error('"Authentication failed !"')
    return render_template('login.html', title='Login', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(port=8080, debug=True)
