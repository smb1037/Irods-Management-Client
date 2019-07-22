import os # For connecting to iRODS
import ssl # For connecting to iRODS
from flask import render_template, flash, redirect, request, url_for, send_from_directory
from app import app
from app.forms import LoginForm, NewCollectionForm, ModifyCollectionForm, SearchForm
from flask_login import UserMixin, login_required, current_user, login_user
#File upload
#def allowed

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
#@login_required

def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
   form=LoginForm(request.form)
#trying to authenticate users.
   authenticated=True
   if request.method=='POST':
      hostName=request.form['hostName']
      portNumber=request.form['portNumber']
      userName=request.form['userName']
      irodsZone=request.form['irodsZone']
      password=request.form['password']
      try:
         with iRODSSession(host=hostName, port=portNumber, user=userName, password=password, zone=irodsZone) as session:
            pass
            return render_template('search.html', title='Sign In', form=form)
      except:
         flash('Login Failed')
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

@app.route('/modifyCollection', methods=['GET', 'POST'])
#@login_required
def modifyCollection():
   form = ModifyCollectionForm(request.form)
   if request.method=='POST':
      modifyCollectionName = request.form['modifyCollectionName']
      Attribute = request.form['Attribute']
      Value = request.form['Value']
      obj=session.data_objects.create("/tempZone/home/rods/"+modifyCollectionName+"/"+Attribute)
      with obj.open('a') as f:
         f.write(Value +'\n')

   return render_template('modifyCollection.html', title='Modify Collection', form=form)

@app.route('/search', methods=['GET', 'POST'])
#@login_required
def search():
   form = SearchForm(request.form)
   if request.method == 'GET':
      parentColl=session.collections.get("/tempZone/home/rods")
      collectionList = parentColl.subcollections
      return render_template('search.html', title='Search', form=form, len=len(collectionList),collectionList=collectionList)
   if request.method=='POST':
      searchCollName=request.form['searchCollection']
      coll = session.collections.get("/tempZone/home/rods/"+searchCollName)
      collObjects=coll.data_objects
      return render_template('displayCollection.html', form=form, len=len(collObjects),  collObjects=collObjects)
   else:
      return render_template('search.html', title='Search', form=form)
