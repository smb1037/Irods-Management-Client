import os # For connecting to iRODS
import ssl # For connecting to iRODS
from flask import render_template, flash, redirect, request, url_for, send_from_directory
from app import app
from app.forms import LoginForm, NewCollectionForm, ModifyCollectionForm, SearchForm
from flask_login import UserMixin, login_required, current_user, login_user

#File upload
#def allowed

#----------------- Establishing Connection ----------------------
#from irods.session import iRODSSession
#try:
#	env_file=os.environ['IRODS_ENVIRONMENT_FILE']
#except KeyError:
#	env_file = os.path.expanduser('~/.irods/irods_environment.json')

#ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
#ssl_settings = {'ssl_context': ssl_context}
#with iRODSSession(irods_env_file=env_file, **ssl_settings) as session:
#	with iRODSSession(irods_env_file=env_file) as session:
#		pass
#----------------- END CONNECTION ATTEMPT---------------------------

@app.route('/')
@app.route('/index')
#@login_required

def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
#trying to authenticate users.
    #if current_user.is_authenticated:
       # return redirect(url_for('index')
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/newCollection', methods=['GET', 'POST'])
#@login_required
def newCollection():
   form=NewCollectionForm(request.form)
   if request.method=='POST':
      collectionName = request.form['collectionName']
      coll = session.collections.create("/tempZone/home/rods/"+collectionName)
   return render_template('newCollection.html', title='New Collection', form=form)

#--------------THIS IS THE WORKING CODE--------------------
#form = NewCollectionForm()
   #coll = session.collections.create("/tempZone/home/rods/pleaseWork")
   #return render_template('newCollection.html', title='New Collection', form=form)

@app.route('/modifyCollection')
#@login_required
def modifyCollection():
   form = ModifyCollectionForm()
   return render_template('modifyCollection.html', title='Modify Collection', form=form)

@app.route('/search')
#@login_required
def search():
   form = SearchForm()
   return render_template('search.html', title='Search', form=form)
