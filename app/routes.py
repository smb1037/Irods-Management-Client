import os # For connecting to iRODS
import ssl # For connecting to iRODS
from flask import render_template, flash, redirect, request
from app import app
from app.forms import LoginForm, NewCollectionForm, ModifyCollectionForm, SearchForm
#----------------- Establishing Connection ----------------------
from irods.session import iRODSSession
try:
	env_file=os.environ['IRODS_ENVIRONMENT_FILE']
except KeyError:
	env_file = os.path.expanduser('~/.irods/irods_environment.json')

ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
ssl_settings = {'ssl_context': ssl_context}
with iRODSSession(irods_env_file=env_file, **ssl_settings) as session:
	with iRODSSession(irods_env_file=env_file) as session:
		pass
#----------------- END CONNECTION ATTEMPT---------------------------

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/newCollection')
def newCollection():
   form = NewCollectionForm()
#---Creating new collection-----------
   coll = session.collections.create("/tempZone/home/rods/TestDir")
   return render_template('newCollection.html', title='New Collection', form=form)

@app.route('/modifyCollection')
def modifyCollection():
   form = ModifyCollectionForm()
   return render_template('modifyCollection.html', title='Modify Collection', form=form)

@app.route('/search')
def search():
   form = SearchForm()
   return render_template('search.html', title='Search', form=form)
