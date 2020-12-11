# Flask
Flask with Python

1. app.run(port=8888, debug=True): Debug model will restart app automatically.
1. @app.route to add routes
1. import render_template to return html 
1. download boilerplate HTML files from initializr.com
1. url_for function in html in href
1. Jinja template: {% extends "base.html" %} {% block %} as placeholders 
1. multiple routes point to the same route function
1. Error handling with @app.errorhandler
1. POST request by methods=['GET', 'POST']. Use request.form[] to get data
1. url_for('static', filename = 'css/main.css') to point to static resource
1. logging information
1. redirect to another page
1. {% with %} statement in Jinja lets you define variable, but limits the scope of a variable with the {% endwith %} 
1. Add css to style flash
1. WTForm and validators
1. Command:
    > from app import db, User
    db.create_all()
    db.session.add()
    db.session.commit()
    User.query.all()
    User.query.first()
    User.query.filter_by(username='admin').all()
    db.drop_all()
