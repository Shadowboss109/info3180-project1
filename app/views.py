"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, send_from_directory, url_for
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app.forms import ContactForm
from sys import platform

from app.model import PropertyModel

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


#/properties/create

@app.route('/properties/create', methods=['POST', 'GET'])
def properties_create():
   
    # Instantiate your form class
    form = ContactForm()
    filefolder = '/uploads'
    # Validate file upload on submit
    if request.method == 'POST':
        # Get file data and save to your uploads folder
        if form.validate_on_submit():  
            property_title = form.title.data
            description = form.description.data
            num_of_bedrooms= form.rooms.data
            num_of_bathrooms = form.bathrooms.data
            price = form.price.data
            location = form.location.data
            property_type = form.property_type.data

            photo = form.photo.data            
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(os.getcwd(),"uploads", filename)) 


            
            property = PropertyModel(
                title=property_title,
                description=description,
                num_of_bedrooms=num_of_bedrooms,
                num_of_bathrooms=num_of_bathrooms,
                price=price,
                location=location,
                property_type=property_type,
                property_name=filename
            )
            db.session.add(property)
            db.session.commit()

            flash('You property data has been successfully uploaded', 'success')
            return redirect(url_for('properties'))
    return render_template('properties_create.html', form= form)

#properties

@app.route('/properties')
def properties():
    properties = PropertyModel.query.all()
    return render_template('properties.html', properties= properties)


@app.route('/properties/<propertyid>')
def get_image(propertyid):
    return send_from_directory(app.config['UPLOAD_FOLDER'],propertyid)

@app.route('/property/<propertyid>')
def property(propertyid): 
    search = PropertyModel.query.filter_by(title=propertyid).first()  
    return render_template('property.html',search=search) 
    


def get_uploaded_images():
    image_list=[]
    rootdir = os.getcwd()
    if platform=="win32":
        for subdir, dirs, files in os.walk(rootdir + '\\uploads'):
            for file in files:
                image_list+=[file]
            return image_list
        return image_list
    else:
        for subdir, dirs, files in os.walk(rootdir + '/uploads'):
            for file in files:
                image_list+=[file]
            return image_list
        return image_list     
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




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
