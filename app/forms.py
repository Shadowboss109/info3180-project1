#imports
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,FileField, SelectField, IntegerField,DecimalField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed



#ContactForm class
class ContactForm(FlaskForm):
    #class Meta:
     #   csrf = True

    title=StringField('Property Title', validators=[DataRequired()])
        
    description = TextAreaField('Description', validators=[DataRequired()])

    rooms =  IntegerField("No. of Rooms", validators=[DataRequired()])

    bathrooms =  IntegerField("No. of Bathrooms", validators=[DataRequired()])

    price = DecimalField("Price", validators=[DataRequired()],places=2)

    location=StringField('Location', validators=[DataRequired()])

    photo = FileField("Photo",validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

    property_type=SelectField("Property Type", choices=["House", "Apartment"])