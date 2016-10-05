from flask import Blueprint,render_template,request
from app import models
from app import db
admin = Blueprint('auth',__name__)

@admin.route('/')
def index():
	return render_template('index.html')

@admin.route('/login')
def login():
	return render_template('login.html')

@admin.route('/register')
def register():
	return render_template('register.html')

@admin.route('/terms')
def terms():
	return render_template('terms.html')

@admin.route('/privacy')
def privacy():
	return render_template('privacy.html')

@admin.route('/about')
def about():
	return render_template('about.html')

@admin.route('/process', methods = ['GET','POST'])
def process():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	username = request.form['username']
	password = request.form['pwd']
	cnf_password = request.form['cnf_pwd']

	newUser = models.User(firstname = first_name, lastname = last_name, email = email, password = password, username = username)
	db.session.add(newUser)
	db.session.commit()

	return render_template('me.html', name = first_name)
