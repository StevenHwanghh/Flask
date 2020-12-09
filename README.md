# Flask
Flask with Python

1. app.run(port=8888, debug=True): Debug model will restart app automatically.
2. @app.route to add routes
3. import render_template to return html 
4. download boilerplate HTML files from initializr.com
5. url_for function in html in href
6. Jinja template: {% extends "base.html" %} {% block %} as placeholders 
7. multiple routes point to the same route function
8. Error handling with @app.errorhandler
9. POST request by methods=['GET', 'POST']. Use request.form[] to get data
10. url_for('static', filename = 'css/main.css') to point to static resource
11. logging information
12. redirect to another page
13. {% with %} statement in Jinja lets you define variable, but limits the scope of a variable with the {% endwith %} 
14. Add css to style flash
15. WTForm and validators