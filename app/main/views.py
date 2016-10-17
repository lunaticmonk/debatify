from flask import Blueprint,render_template,request,flash,g,redirect,url_for
from app import db,moment
from app.models import User,Question,load_user
from flask_login import current_user
from flask_moment import Moment
from datetime import datetime



welcome = Blueprint('main',__name__, template_folder = "templates")

@welcome.route('/', methods = ["GET","POST"])
def index():
	savedQuestion = request.form['topic-textarea']
	savedTopic = request.form['question-textarea']
	topicandquestion = Question(topic = savedTopic,questions = savedQuestion, owner = current_user)
	db.session.add(topicandquestion)
 	db.session.commit()
	return render_template('listitems.html', topic = savedTopic, questions = savedQuestion)
	#return redirect(url_for('auth.loginprocess'))

@welcome.route('/profile', methods = ['GET','POST'])
def profile():
	return render_template('user.html', user = current_user)

@welcome.route('/edit_profile', methods = ['GET','POST'])
def edit():
	return render_template('edit_profile.html', user = current_user)
	# 	current_user.firstname = request.form['firstname']
	# 	current_user.lastname = request.form['lastname']
	# 	current_user.about_me = request.form['about_me']
	# 	current_user.location = request.form['loaction']
	# 	db.session.add(user)
	# 	db.session.commit()
	# return render_template('user.html', user = current_user)

@welcome.route('/update_profile', methods = ['GET','POST'])
def update_profile():
	user = current_user
	current_user.firstname = request.form['firstname']
	current_user.lastname = request.form['lastname']
	current_user.about_me = request.form['about_me']
	current_user.location = request.form['location']
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('main.profile'))