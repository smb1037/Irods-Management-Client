import os #For connecting to iRODS
import ssl # For connecting to iRODS
from irods.session import iRODSSession # Getting the iRODS session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, TextField
from wtforms.validators import DataRequired

#------------Trying to connect to iRODS---------------
try:
	env_file=os.environ['IRODS_ENVIRONMENT_FILE']
except KeyError:
	env_file = os.path.expanduser('~/.irods/irods_environment.json')

ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
ssl_settings = {'ssl_context': ssl_context}
with iRODSSession(irods_env_file=env_file, **ssl_settings) as session:
	with iRODSSession(irods_env_file=env_file) as session:
		pass

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
   modifyCollectionName = StringField('Name of Collection: ', validators=[DataRequired()])
   Attribute = StringField('Attribute:', validators=[DataRequired()])
   Value = StringField('Values:', validators=[DataRequired()])
   submit = SubmitField('Modify Collection')

class SearchForm(FlaskForm):
   searchCollection = StringField('Enter Collection Name: ', validators=[DataRequired()])
   submit = SubmitField('Submit')
   showFields = SubmitField('Show Collections')
