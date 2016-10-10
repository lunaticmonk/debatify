from flask import Blueprint,render_template,request,flash,redirect,url_for,session,g
from flask_login import login_required,login_user,logout_user
from app import models,login_manager
from app import db

#app.config['DEBATIFY_ADMIN']=<'somunimkarde@gmail.com'>

admin = Blueprint('auth',__name__, template_folder = "templates")

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
	if(models.User.query.filter_by(email = email).first()):
		return '<p>Already registered with this email.Please login to continue.</p>'
	else:
		newUser = models.User(firstname = first_name, lastname = last_name, email = email, password = password, username = username)
		session['known'] = False
		db.session.add(newUser)
		db.session.commit()
		# if app.config['DEBATIFY_ADMIN']:
		# 	send_email(app.config['DEBATIFY_ADMIN'],'New User','mail/new_user',user = newUser)

		#return render_template('me.html', name = first_name)
		return "<p>You are registered successfully.Please login to continue</p>"

@admin.route('/me',methods = ['GET','POST'])
def loginprocess():
	g.user = models.User.query.filter_by(email = request.form['Email']).first()
	password = request.form['Password']
	if g.user is not None and g.user.verify_password(password):
		login_user(g.user)
		return render_template('me.html', firstname = g.user.firstname)
	else:
		flash('Invalid login')
		return render_template('login.html')

@admin.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('auth.login'))


# @admin.route('/secret')
# @login_required
# def secret():
# 	return 'Only authenticated Users allowed'