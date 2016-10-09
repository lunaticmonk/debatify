from flask import Blueprint,render_template,request,flash,g
from flask.ext.login import login_required,login_user,logout_user,current_user
from app import models,login_manager
from app import db
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
		db.session.add(newUser)
		db.session.commit()

		#return render_template('me.html', name = first_name)
		return "<p>You are registered successfully.Please login to continue</p>"


@admin.route('/me',methods = ['GET','POST'])
def loginprocess():
	user = models.User.query.filter_by(email = request.form['Email']).first()
	password = request.form['Password']
	if user is not None and user.verify_password(password):
		#user_id = user.query.filter_by(password = password).first()
		#g.user = user
		user.authenticated = True
		user = current_user
		login_user(user)
		issues = models.Question.query.filter_by(current_user.id).all()
		return render_template('me.html', name = user.firstname, issues = issues)
	else:
		#flash('Invalid login')
		return render_template('login.html')

# @admin.route('/logout')
# @login_required
# def logout():
# 	logout_user()
# 	flash('You have been logged out.')
# 	return redirect(url_for('auth.login'))

# @admin.route('/welcome', methods = ['GET','POST'])
# def welcome():
# 	fetchedTopic = request.form['topic-textarea']
# 	fetchedQuestion = request.form['question-textarea']
# 	# user = g.user
# 	#return user.firstname
# 	topicandquestion = models.Question(topic = fetchedTopic,questions = fetchedQuestion, owner = models.load_user())
# 	db.session.add(topicandquestion)
# 	db.session.commit()
# 	#return '<p>hello</p>'
# 	return render_template('listitems.html', topic = fetchedTopic)
# 	#return "<p>hello</p>"

@admin.route('/secret')
@login_required
def secret():
	return 'Only authenticated Users allowed'