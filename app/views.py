"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app.forms import ContactForm
from sys import platform

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Theodore Bennett")



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404




@app.route('/properties/create', methods=['POST', 'GET'])
def properties_create():
   
    # Instantiate your form class
    form = ContactForm()
    filefolder = './uploads'
    # Validate file upload on submit
    if request.method == 'POST':
        # Get file data and save to your uploads folder
        if form.validate_on_submit():          
            file = form.photo.data      
            filename = secure_filename(file.filename)
            file.save(os.path.join(filefolder, filename))     
            flash('File Saved', 'success')
            return redirect(url_for('home'))
    return render_template('properties_create.html', form= form)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
