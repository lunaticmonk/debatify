from flask import Blueprint,render_template,request,flash,g,redirect,url_for
from app import db
from app.models import User,Question,load_user
from flask_login import current_user

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