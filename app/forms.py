import os #For connecting to iRODS
import ssl # For connecting to iRODS
from irods.session import iRODSSession # Getting the iRODS session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

#------------Trying to connect to iRODS---------------
#------------------ Connection block end ----------------------------


class LoginForm(FlaskForm):
    hostName = StringField('Enter the host name (DNS) of the server to connect to:', validators=[DataRequired()])
    portNumber = IntegerField('Please enter the port number:', validators=[DataRequired()])
    userName = StringField('Enter your irods user name:', validators=[DataRequired()])
    irodsZone = StringField('Enter your irods zone:', validators=[DataRequired()])
    password = PasswordField('Enter your current irods password:', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class NewCollectionForm(FlaskForm):
   collectionName = StringField('Enter collection name:', validators=[DataRequired()])
   attributesAndValues = StringField('Attributes and values:', validators=[DataRequired()])
   submit = SubmitField('Create new collection')

class ModifyCollectionForm(FlaskForm):
   attributesAndValues = StringField('Attributes and values:', validators=[DataRequired()])
   submit = SubmitField('Modify Collection')

class SearchForm(FlaskForm):
   collect = SelectField(u'Collections' , choices = [('number1', 'NUMBER1'), ('number2', 'NUMBER2')])
   submit = SubmitField('Submit')
