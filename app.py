import os
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from logging import DEBUG

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(port=8080, debug=True)
